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
if [ -L "data/web_static/current" ]; then
echo "suppression du liens symbolic"
unlink data/web_static/current
fi
echo création du liens
ln -s data/web_static/releases/test/ data/web_static/current
chown -hR ubuntu:ubuntu /data/
sudo location /hbnb_static/
{
    alias /data/web_static/current/;
    autoindex off;           ↑
}
service nginx restart