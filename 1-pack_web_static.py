#!/usr/bin/python3

"""
Create an .tgz archive with all the statoc content of
my AirBnB static clone
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
        local('tar -czvf versions/web_static_{}.tgz web_static'.format(complete))
        return 'versions/web_static_{}.tgz'.format(comlete)
    except(Exception):
        return None
