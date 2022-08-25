#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "Hello darkness my old friend" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
sed -i '/^\tserver_name/ a\\n\tlocation \/hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
