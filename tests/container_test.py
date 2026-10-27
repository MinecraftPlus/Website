"""End-to-end checks for a built image. Requires Python 3 and Docker only."""

import argparse
import hashlib
import json
import subprocess
import time
import urllib.error
import urllib.request
from contextlib import ExitStack, contextmanager
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def docker(*args, input=None, check=True):
    result = subprocess.run(
        ["docker", *args], input=input, capture_output=True, text=True, timeout=90
    )
    if check and result.returncode:
        raise AssertionError(f"docker {' '.join(args)}: {result.stderr or result.stdout}")
    return result.stdout.strip()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for key, value in attrs if key in ("href", "src") and value)


class Container:
    def __init__(self, image):
        self.id = docker("run", "-d", "-p", "127.0.0.1::80", image)
        self.image = image
        self.opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({}), NoRedirect()
        )

    def request(self, path, headers=None):
        port = docker("port", self.id, "80/tcp").rsplit(":", 1)[1]
        request_headers = {"Host": "website.test", "Accept-Language": "en"}
        request_headers.update(headers or {})
        request_headers = {key: value for key, value in request_headers.items() if value is not None}
        request = urllib.request.Request(
            f"http://127.0.0.1:{port}{path}", headers=request_headers
        )
        try:
            response = self.opener.open(request, timeout=5)
        except urllib.error.HTTPError as error:
            response = error
        with response:
            return response.status, response.headers, response.read()

    def ready(self):
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            try:
                status, _, body = self.request("/en")
                if status == 200 and b'MinecraftPlus' in body:
                    return
            except (OSError, urllib.error.URLError):
                pass
            if self.state()["Status"] == "exited":
                break
            time.sleep(0.2)
        raise AssertionError(f"{self.image} did not start:\n{docker('logs', self.id)}")

    def state(self):
        return json.loads(docker("inspect", "--format", "{{json .State}}", self.id))

    def wait_exit(self):
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            state = self.state()
            if not state["Running"]:
                return state["ExitCode"]
            time.sleep(0.1)
        raise AssertionError(f"Container did not exit:\n{docker('logs', self.id)}")


@contextmanager
def running(image):
    container = Container(image)
    try:
        container.ready()
        yield container
    except BaseException:
        print(docker("logs", container.id, check=False))
        raise
    finally:
        docker("rm", "-f", container.id, check=False)


def page_checks(container, reference):
    paths = (
        "/en", "/pl", "/en/status", "/pl/updates", "/en/download",
        "/en/updates/released/cannon-update", "/en/", "/en?source=migration&test=1",
        "/?en", "/index.php?pl", "/en/no-such-page", "/pl/no-such-page",
    )
    for path in paths:
        status, headers, body = container.request(path)
        expected = 404 if "no-such-page" in path else 200
        require(status == expected, f"{path}: expected {expected}, got {status}")
        require(b"MinecraftPlus" in body, f"{path}: not a rendered Pico page")
        require(b"<?php" not in body, f"{path}: PHP source leaked")
        if reference:
            old_status, _, old_body = reference.request(path)
            require((status, body) == (old_status, old_body), f"Apache/nginx response differs: {path}")

    for language, target in (("pl-PL", "pl"), ("en-US", "en"), (None, "en")):
        request_headers = {"Accept-Language": language}
        status, headers, _ = container.request("/", request_headers)
        require(status == 302 and headers["Location"] == target, f"Language redirect: {language}")
        if reference:
            old_status, old_headers, _ = reference.request("/", request_headers)
            require((status, headers["Location"]) == (old_status, old_headers["Location"]), "Redirect differs")

    for forwarded, origin in (
        ({}, "http://website.test"),
        ({"X-Forwarded-Proto": "https"}, "https://website.test"),
        ({"X-Forwarded-Proto": "https", "X-Forwarded-Port": "443"}, "https://website.test"),
        ({"Host": "website.test:8443", "X-Forwarded-Proto": "https", "X-Forwarded-Port": "8443"}, "https://website.test:8443"),
        ({"X-Forwarded-Proto": "https, http"}, "https://website.test"),
    ):
        status, _, body = container.request("/en/status", forwarded)
        require(status == 200, "Proxy request failed")
        require(f'rel="canonical" href="{origin}/en/status"'.encode() in body, f"Wrong canonical for {forwarded}")
        links = Links()
        links.feed(body.decode())
        local_links = [url for url in links.urls if "website.test" in url]
        require(local_links and all(url.startswith(origin + "/") for url in local_links), f"Wrong public origin: {local_links}")
        if reference:
            old_status, _, old_body = reference.request("/en/status", forwarded)
            require((status, body) == (old_status, old_body), f"Proxy response differs: {forwarded}")

    status, headers, _ = container.request("/themes/mcplus", {"X-Forwarded-Proto": "https"})
    require(status == 301 and headers["Location"] == "/themes/mcplus/", "Directory redirect exposes internal origin")


def asset_checks(container):
    cases = {
        "themes/mcplus/css/style.css": "text/css",
        "themes/mcplus/js/utils.js": "javascript",
        "themes/mcplus/img/flags/pl.png": "image/png",
        "themes/mcplus/font/DroidSans-Regular.woff2": "font/woff2",
        "themes/mcplus/font/DroidSans-Regular.woff": "font/woff",
        "themes/mcplus/font/DroidSans-Regular.eot": "application/vnd.ms-fontobject",
        "assets/images/cannon-update_cannon-back.png": "image/png",
        "assets/videos/cannon-update_cannon-steering.mp4": "video/mp4",
        "plugins/TableOfContents/style.css": "text/css",
        "favicon.ico": "image/",
    }
    for path, mime in cases.items():
        status, headers, body = container.request("/" + path + "?v=test")
        require(status == 200 and mime in headers["Content-Type"], f"Invalid static response: {path}, {headers}")
        require(hashlib.sha256(body).digest() == hashlib.sha256((ROOT / path).read_bytes()).digest(), f"Asset changed: {path}")
    status, headers, body = container.request(
        "/assets/videos/cannon-update_cannon-steering.mp4", {"Range": "bytes=0-31"}
    )
    require(status == 206 and len(body) == 32 and headers["Content-Range"].startswith("bytes 0-31/"), "Video range request failed")
    for path in ("/assets/", "/themes/mcplus/"):
        status, _, body = container.request(path)
        require(status == 403 and b"Index of" not in body, f"Directory listing enabled: {path}")


def security_checks(container):
    protected = (
        "/config/config.yml", "/content/en/index.md", "/vendor/autoload.php",
        "/language/pl.php", "/composer.json", "/composer.lock", "/composer.phar",
        "/CHANGELOG.md", "/.git/config", "/.htaccess", "/assets/.hidden",
        "/themes/mcplus/tmpl/index.twig", "/themes/mcplus/pico-theme.yml",
        "/plugins/MultiLanguage/MultiLanguage.php", "/Dockerfile", "/docker/nginx.conf",
        "/tests/container_test.py", "/config%2fconfig.yml",
    )
    docker("exec", container.id, "mkdir", "-p", "/var/www/html/.well-known/acme-challenge")
    docker("exec", "-i", container.id, "tee", "/var/www/html/.well-known/acme-challenge/probe", input="acme-probe")
    docker("exec", "-i", container.id, "tee", "/var/www/html/assets/.hidden", input="hidden-probe")
    status, _, body = container.request("/.well-known/acme-challenge/probe")
    require(status == 200 and body == b"acme-probe", ".well-known exception broken")
    for suffix in ("php", "PHP", "php5", "phtml", "phar"):
        path = "/assets/migration-probe." + suffix
        docker("exec", "-i", container.id, "tee", "/var/www/html" + path,
               input="<?php file_put_contents('/tmp/unexpected-php-execution', 'executed'); echo 'PHP_EXECUTED';")
        protected += (path, path + "/extra")
    for path in protected:
        status, _, body = container.request(path)
        require(status == 404 and b"Error 404" in body, f"Protected path did not reach Pico 404: {path}, {status}")
        require(b"<?php" not in body and b"hidden-probe" not in body, f"Source leaked: {path}")
    docker("exec", container.id, "test", "!", "-e", "/tmp/unexpected-php-execution")
    docker("exec", container.id, "sh", "-c", "test ! -e /var/www/html/.git && test ! -e /var/www/html/docker && test ! -e /var/www/html/tests && test ! -e /usr/local/bin/composer")
    listeners = docker("exec", container.id, "ss", "-ltn")
    require("127.0.0.1:9000" in listeners and "0.0.0.0:9000" not in listeners and "*:9000" not in listeners, "PHP-FPM is exposed")
    lock_hash = docker("exec", container.id, "sha256sum", "/var/www/html/composer.lock").split()[0]
    require(lock_hash == hashlib.sha256((ROOT / "composer.lock").read_bytes()).hexdigest(), "Dependency lock changed")
    for path in ("plugins/MultiLanguage/MultiLanguage.php", "plugins/TableOfContents/TableOfContents.php"):
        actual = docker("exec", container.id, "sha256sum", "/var/www/html/" + path).split()[0]
        require(actual == hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), f"Repository plugin override lost: {path}")


def health_checks(container):
    docker("exec", container.id, "/usr/local/bin/healthcheck.sh")
    deadline = time.monotonic() + 40
    while time.monotonic() < deadline:
        if container.state()["Health"]["Status"] == "healthy":
            return
        time.sleep(0.5)
    raise AssertionError("Docker healthcheck did not become healthy")


def lifecycle_checks(image):
    for server, pid_file in (("nginx", "/run/nginx.pid"), ("PHP-FPM", "/usr/local/var/run/php-fpm.pid")):
        with running(image) as container:
            docker("exec", container.id, "sh", "-c", 'kill -KILL "$(cat ' + pid_file + ')"')
            require(container.wait_exit() != 0, f"{server} failure did not stop the container with an error")
        print(f"PASS: {server} failure stops the container")
    with running(image) as container:
        docker("stop", "--time", "10", container.id)
        require(container.state()["ExitCode"] == 0, "Graceful shutdown failed or timed out")
    print("PASS: graceful shutdown")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", help="locally built nginx image")
    parser.add_argument("--reference", help="optional Apache image built from the same source and lock file")
    args = parser.parse_args()
    with ExitStack() as stack:
        reference = stack.enter_context(running(args.reference)) if args.reference else None
        container = stack.enter_context(running(args.image))
        for name, check in (
            ("pages, languages and public URLs", lambda: page_checks(container, reference)),
            ("assets and video ranges", lambda: asset_checks(container)),
            ("file protection and plugin overrides", lambda: security_checks(container)),
            ("application healthcheck", lambda: health_checks(container)),
        ):
            check()
            print(f"PASS: {name}", flush=True)
    lifecycle_checks(args.image)


if __name__ == "__main__":
    main()
