#!/usr/bin/env bash
# Script that sets up your web servers for deployment
apt update -y
apt install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir /data/web_static/shared/
printf %s "<html>
  <head>
  </head>
  <body>
    Test text
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart
