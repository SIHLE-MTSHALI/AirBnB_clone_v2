#!/usr/bin/python3
"""
This module defines a Fabric script that distributes an archive to web servers.
The script automates the deployment of web_static contents to specified servers.
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Add actual IP addresses

def do_deploy(archive_path):
    """
    Deploys an archive to web servers.
    Returns True if all operations are done correctly, otherwise returns False.
    """
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/" + no_ext + "/"
        # Upload the archive to the /tmp/ directory of the server
        put(archive_path, "/tmp/")
        # Uncompress the archive to the folder on the server
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, path))
        run("rm /tmp/{}".format(file_name))
        # Move content to the parent directory
        run("mv {}/web_static/* {}".format(path, path))
        run("rm -rf {}/web_static".format(path))
        # Delete the symbolic link /data/web_static/current from the server
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link
        run("ln -s {} /data/web_static/current".format(path))
        print("New version deployed!")
        return True
    except:
        return False
