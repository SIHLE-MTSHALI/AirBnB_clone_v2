# Puppet manifest to set up web servers for deployment of web_static

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "<html><head></head><body>Hello World!</body></html>",
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location /hbnb_static {
            alias /data/web_static/current;
        }
    }
  ",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure => 'running',
  enable => true,
}
