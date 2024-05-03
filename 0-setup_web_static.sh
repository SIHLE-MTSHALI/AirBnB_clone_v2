#!/usr/bin/env bash
# Sets up web servers for deployment of web_static

# Install Nginx if not already installed
if [ ! -x /usr/sbin/nginx ]; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create fake HTML file for testing
echo "<html><head></head><body>Hello World!</body></html>" > /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
