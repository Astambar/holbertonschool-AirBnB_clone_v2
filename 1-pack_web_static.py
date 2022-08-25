#!/usr/bin/python3

"""
Create an .tgz archive with all the statoc content of
my AirBnB static clone
"""

from fabric.api import local
import time


def do_pack():
    """
    La fonction do_pack crée une archive contenant le dossier web_static.
    Il renvoie le nom de l'archive qu'il a créée,
    ou None en cas d'erreur.

    :return: Le chemin vers le fichier archive
    :doc-author: Trelent
    """
    complete = time.strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        local('tar -czvf versions/web_static_{}.tgz web_static'.format(complete
                                                                       ))
        return 'versions/web_static_{}.tgz'.format(complete)
    except Exception:
        return None
