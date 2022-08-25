#!/usr/bin/python3

"""
Créez une archive .tgz avec tout le contenu statoc de
mon clone statique AirBnB
"""

from fabric.api import local
import time

def do_pack():
    date = time.strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        local('tar -czvf versions/web_static_{}.tgz web_static'.format(date))
        return 'versions/web_static_{}.tgz'.format(date)
    except Exception:
        return None
