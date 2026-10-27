# MinecraftPlus website

The MinecraftPlus project website uses Pico CMS 2.1, Markdown content in English
and Polish, and the `mcplus` Twig theme. It needs no database or administration
backend.

## Build and run

Requires Docker with Linux containers. The image runs PHP 8.5.12 on Debian
Bookworm; running the application outside Docker requires PHP 8.5 or newer
(within PHP 8.x). Build from the repository root:

```sh
docker build -t mcplus-website:local .
docker run -d --name mcplus-website -p 127.0.0.1:8080:80 mcplus-website:local
```

Visit <http://localhost:8080/en> or <http://localhost:8080/pl>. The root URL
redirects according to `Accept-Language`, falling back to English.

One container runs nginx and PHP-FPM, managed by a Bash wrapper under `tini`.
Only HTTP port 80 needs publishing. PHP-FPM listens on the container's loopback
address, `127.0.0.1:9000`; do not publish port 9000. The inherited PHP image may
still list that unused external port in image metadata.

`composer.lock` preserves the dependencies extracted from the previous Apache
image, `minecraftplus/website@sha256:ad08f5461d974438eb6ae4c79b712090f45bdb06614fae5240dab10c18b702f8`.
The build uses Composer 2.10.3, installs locked dependencies first, and then
overlays the repository's modified plugins and theme. Keep that order when
editing the Dockerfile. PHP `dom` and `mbstring` are checked during the build.
No dependencies are installed at container startup.

## HTTP and reverse proxy configuration

TLS remains on the existing external reverse proxy. Forward requests to
container port 80, preserving the public `Host` header, including a nonstandard
public port if one is used. The proxy must **overwrite** client-supplied
`X-Forwarded-Proto` and `X-Forwarded-Port` with the public scheme and port.
Restrict production access to the container to that trusted proxy: the PHP entry
point trusts these headers. Configure the proxy to preserve the original public
path; the application is served at the domain root.

nginx preserves the original request URI and query string when routing pages to
`index.php`. Pico has `rewrite_url: true`; generated links use paths such as
`/en/status`, while older `/?en` URLs continue to work. Automatic nginx directory
redirects use relative locations so they preserve the public scheme and port.

Only the root `index.php` is executable through FastCGI. Internal configuration,
content, dependencies, language sources, dotfiles and source templates are routed
to Pico's 404 page before any static-file handling. Static images, scripts,
styles, fonts and videos remain accessible, including plugin stylesheets. Directory
listing is disabled. The `.well-known` exception permits static challenge files;
certificate provisioning remains the external proxy's responsibility.

Server configuration and startup scripts live in `docker/` and are copied outside
the document root. Apache and `.htaccess` are no longer used. There is no FastCGI
response cache, so language negotiation retains its existing behavior.

## Tests and operations

Requires Python 3 and access to Docker; no Python packages need installing:

```sh
python tests/container_test.py mcplus-website:local
```

The suite starts isolated containers on temporary loopback ports and removes
them afterwards. It checks page rendering, language redirects, legacy URLs,
query strings, canonical/alternate links behind HTTPS proxies (including a custom
port), 404s, static-file bytes and MIME types, video range requests, protection of
internal files and arbitrary PHP scripts, plugin overrides, application health,
process failure handling and graceful shutdown. It also verifies PHP 8.5,
checks logs for runtime warnings/errors and preserves the existing Polish
heading anchors. The table-of-contents plugin explicitly uses the old `C`
transliteration locale while generating anchors, restoring the original locale
afterwards; PHP 8's default `C.UTF-8` would otherwise change public fragment URLs.

To compare HTML responses with an Apache reference built from the same application
source and lock file:

```sh
python tests/container_test.py mcplus-website:local --reference mcplus-website:apache-reference
```

The migration was compared against a local Apache reference created by overlaying
the pre-migration working tree on the previous image above. An unrelated or older
application revision is unsuitable for byte-for-byte comparisons. For the PHP
upgrade, the previous nginx/PHP 7.4 image was retained locally as
`mcplus-website:php74-reference` and used with the same `--reference` option;
rendered page responses remain identical.

GitHub Actions builds and loads a candidate image, runs the suite, and publishes
the **same image** only after tests pass on a push to `master`. Pull requests only
build and test. Images are published to `minecraftplus/website` with `latest`
and timestamp tags (`YYYYMMDD-HHmmss`).

```sh
docker logs --follow mcplus-website
docker inspect --format '{{json .State.Health}}' mcplus-website
docker exec mcplus-website /usr/local/bin/healthcheck.sh
docker stop --time 10 mcplus-website
```

Health checks render `/en` through nginx and PHP-FPM every 30 seconds, with a
20-second startup grace period and three retries. Logs go to stdout/stderr. If
either server exits unexpectedly, the wrapper stops its peer and exits with an
error. Docker `stop` gracefully stops both servers within the default timeout.
An unhealthy status alone does not restart a container; use the deployment
platform's health monitoring and restart policy.

## Cutover and rollback

Before replacing an existing deployment, record its exact image digest or retain
its timestamp tag. Keep its network, mounts, environment and restart settings.
Run the nginx candidate alongside it on a separate internal port, execute the
test suite and check the real proxy's redirects, canonical URLs, assets and logs.
Then switch the proxy upstream to the candidate. Monitor health, nginx/PHP errors
and unexpected 4xx/5xx responses. Retain the previous container until validation
finishes.

For rollback, point the proxy back to the retained Apache container or recreate
it from its saved image digest and original settings. No database or content
migration is involved. Use an immutable digest for rollback: a mutable tag
such as `latest` can refer to nginx after publication.

The PHP and Composer images are pinned by digest. Bookworm uses its normal signed
package repositories; the former Bullseye archive configuration has been removed.
`composer.json` declares PHP `^8.5` and explicitly permits the Pico installer
plugin. The lock file's platform metadata has been refreshed without changing
the installed package versions.

## Legacy CMS dependencies

This change upgrades PHP and Composer while preserving Pico 2.1 and the existing
theme/plugin APIs. Pico, Twig 1, Symfony YAML 2 and the old Composer installer
still emit deprecation messages under PHP 8.5. Deprecation reporting has not been
disabled to hide them. The container tests fail on PHP warnings, notices, parse
errors and fatal errors; deprecations remain a documented follow-up.

An audit during the PHP upgrade reported 18 existing security advisories affecting
Twig and Symfony YAML. This runtime upgrade does not remediate those dependency
advisories. Updating the CMS and its dependency APIs is a separate migration.
To inspect the current report without changing project files:

```sh
docker run --rm -v "${PWD}:/app:ro" -w /app composer:2 audit --locked --no-plugins
```
