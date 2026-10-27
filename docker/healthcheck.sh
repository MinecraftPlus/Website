#!/usr/bin/env bash
set -euo pipefail

# Check the rendered application, not merely nginx or an open FPM socket.
body=$(curl --fail --silent --show-error --max-time 3 \
    -H 'Host: localhost' -H 'Accept-Language: en' http://127.0.0.1/en)
[[ "$body" == *'MinecraftPlus'* && "$body" == *'rel="canonical"'* ]]
