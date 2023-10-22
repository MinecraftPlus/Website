# Use the official PHP Apache base image
FROM php:7.4-apache

# Update the package list and install system tools
RUN apt-get update && apt-get install -y \
    unzip \
    libzip-dev

# Enable the Apache rewritemod module
RUN a2enmod rewrite

# Copy project files to the /var/www/html directory
COPY . /var/www/html

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --version=2.1.14 --install-dir=/usr/local/bin --filename=composer

# Install Composer dependencies
RUN composer install

# Ensure that the owner of files in the /var/www/html directory is www-data
RUN chown -R www-data:www-data /var/www/html

# Port on which Apache will run
EXPOSE 80

# Start command
CMD ["apache2-foreground"]
