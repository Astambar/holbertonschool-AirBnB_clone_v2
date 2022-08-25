#!/usr/bin/python3

"""
Créez une archive .tgz avec tout le contenu statoc de
mon clone statique AirBnB
"""

from fabric.api import local
import time

def do_pack():
    """
    The do_pack function creates a tarball containing the web_static folder.
    It returns the name of the tarball it created, or None if there was an error.

    :return: The path to the tarball file
    :doc-author: Trelent
    """

    complete = time.strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        local(f'tar -cvzf versions/web_static_{complete}.tgz web_static')
        return f'versions/web_static_{complete}.tgz'
    except(Exception):
        return None
