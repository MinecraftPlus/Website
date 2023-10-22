# Use the official PHP Apache base image
FROM php:7.4-apache

# Update the package list and install system tools
RUN apt-get update && apt-get install -y \
    unzip \
    libzip-dev

# Enable the Apache rewritemod module
RUN a2enmod rewrite

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --version=2.1.14 --install-dir=/usr/local/bin --filename=composer

# Copy composer file to the /var/www/html directory
COPY composer.json /var/www/html/

# Install Composer dependencies
RUN composer install

# Copy project files to the /var/www/html directory
COPY . /var/www/html

# Ensure that the owner of files in the /var/www/html directory is www-data
RUN chown -R www-data:www-data /var/www/html

# Port on which Apache will run
EXPOSE 80

# Start command
CMD ["apache2-foreground"]
