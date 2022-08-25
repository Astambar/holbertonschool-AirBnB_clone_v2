#!/usr/bin/python3

"""
Créez une archive .tgz avec tout le contenu statoc de
mon clone statique AirBnB
"""

from fabric.api import local
from datetime import datetime
date = datetime.now()
complete = date.strftime("%Y%m%d%H%M%S")
def do_pack():
    try:
        local('mkdir -p versions')
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(complete))
        return "versions/web_static_{}.tgz".format(complete)
    except(Exception):
        return None
