#!/usr/bin/python3
"""
Fabric script to generate .tgz archive from web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate .tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None
