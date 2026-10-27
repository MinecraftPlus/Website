FROM composer:2@sha256:b6dcd72ca98fa19d0e5b8476de179859704891fad06dd9e0b96833d4c430a5fc AS composer

FROM php:8.5-fpm-bookworm@sha256:d3db5340c7ecfb1e3a26af5d3d9de8b4e160cdd75692a830b5cb74b0b85db2cf AS base

FROM base AS dependencies

RUN apt-get update \
    && apt-get install -y --no-install-recommends unzip \
    && rm -rf /var/lib/apt/lists/*

COPY --from=composer /usr/bin/composer /usr/local/bin/composer
ENV COMPOSER_ALLOW_SUPERUSER=1

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
