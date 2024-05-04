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
        release_path = "/data/web_static/releases/" + no_ext + "/"
        current_path = "/data/web_static/current"
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, release_path))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}web_static/* {0}'.format(release_path))
        run('rm -rf {}web_static'.format(release_path))
        run('rm -rf {}'.format(current_path))
        run('ln -s {} {}'.format(release_path, current_path))
        return True
    except Exception as e:
        print("Error: {}".format(e))
        return False
