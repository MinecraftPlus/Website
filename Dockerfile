# Keep PHP unchanged while migrating the web server; upgrade it separately.
FROM php:7.4-fpm-bullseye@sha256:3ac7c8c74b2b047c7cb273469d74fc0d59b857aa44043e6ea6a0084372811d5b AS base

# Bullseye security packages have moved off the live security mirror.
COPY docker/debian.sources.list /etc/apt/sources.list

FROM base AS dependencies

RUN apt-get update \
    && apt-get install -y --no-install-recommends unzip \
    && rm -rf /var/lib/apt/lists/*

# Keep the Composer version used to create the Apache reference image.
RUN curl -fsS https://getcomposer.org/installer -o /tmp/composer-setup.php \
    && php /tmp/composer-setup.php --version=2.1.14 --install-dir=/usr/local/bin --filename=composer \
    && rm /tmp/composer-setup.php

WORKDIR /var/www/html
COPY composer.json composer.lock ./
RUN composer install --no-dev --prefer-dist --no-interaction --no-progress \
    && composer check-platform-reqs --no-dev

FROM base AS runtime

RUN apt-get update \
    && apt-get install -y --no-install-recommends nginx-light tini \
    && rm -rf /var/lib/apt/lists/* \
    && rm /etc/nginx/sites-enabled/default

WORKDIR /var/www/html
COPY --from=dependencies /var/www/html/ ./
# Repository plugins intentionally override the versions installed by Composer.
COPY plugins/ ./plugins/
COPY themes/ ./themes/
COPY config/ ./config/
COPY content/ ./content/
COPY language/ ./language/
COPY assets/ ./assets/
COPY index.php favicon.ico ./

COPY docker/nginx.conf /etc/nginx/sites-enabled/website.conf
COPY docker/php-fpm.conf /usr/local/etc/php-fpm.d/zz-website.conf
COPY docker/php.ini /usr/local/etc/php/conf.d/website.ini
COPY docker/start.sh docker/healthcheck.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh /usr/local/bin/healthcheck.sh \
    && php -r 'exit(extension_loaded("dom") && extension_loaded("mbstring") ? 0 : 1);' \
    && nginx -t \
    && php-fpm -t

EXPOSE 80
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 CMD ["/usr/local/bin/healthcheck.sh"]
STOPSIGNAL SIGTERM
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/local/bin/start.sh"]
