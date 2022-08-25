#!/usr/bin/env sh
#install nginx
nginx=$(which nginx)
if [ "$nginx" = "" ]
then
    sudo apt update -y
    sudo apt install nginx -y
fi
#create folder
listFolder="data
			data/web_static/
			data/web_static/releases/
			data/web_static/shared/
			data/web_static/releases/test/"
for element in $listFolder
do
		if [ ! -d $element ];then
		mkdir "$element"
		fi
done
#create file
listFile="data/web_static/releases/test/index.html"
for element in $listFile
do
		if [ ! -f $element ];then
		touch "$element"
		fi
done
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" >> /data/web_static/releases/test/index.html
if [ -L "data/web_static/current" ]; then

unlink data/web_static/current
fi
ln -s data/web_static/releases/test/ data/web_static/current
chown -hR ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
