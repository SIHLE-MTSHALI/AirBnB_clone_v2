#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""
from fabric.api import put, run, env
import os

env.hosts = ['18.210.13.239', '18.214.89.149']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        no_ext = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, no_ext))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
