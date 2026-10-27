#!/usr/bin/env bash
set -euo pipefail

nginx -t
php-fpm -t

nginx_pid=
fpm_pid=
shutdown() {
    trap '' TERM INT QUIT
    # Both servers use QUIT to finish in-flight requests gracefully.
    for pid in "$nginx_pid" "$fpm_pid"; do
        if [[ -n "$pid" ]]; then kill -QUIT "$pid" 2>/dev/null || true; fi
    done
    # Bound shutdown so Docker's default 10-second stop timeout is sufficient.
    for ((attempt = 0; attempt < 80; attempt++)); do
        if ! kill -0 ${nginx_pid:-0} 2>/dev/null && ! kill -0 ${fpm_pid:-0} 2>/dev/null; then
            break
        fi
        sleep 0.1
    done
    for pid in "$nginx_pid" "$fpm_pid"; do
        if [[ -n "$pid" ]]; then kill -KILL "$pid" 2>/dev/null || true; fi
    done
    wait 2>/dev/null || true
}
trap 'shutdown; exit 0' TERM INT QUIT

php-fpm --nodaemonize &
fpm_pid=$!
nginx -g 'daemon off;' &
nginx_pid=$!

# A healthy-looking nginx must never outlive a failed PHP-FPM (or vice versa).
status=0
wait -n "$fpm_pid" "$nginx_pid" || status=$?
echo "A web server process exited unexpectedly (status $status); stopping container" >&2
shutdown
if ((status == 0)); then status=1; fi
exit "$status"
