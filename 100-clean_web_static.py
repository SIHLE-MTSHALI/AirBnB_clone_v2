#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives both locally and on web servers
"""
from fabric.api import *

env.hosts = ['18.210.13.239', '18.214.89.149']

def do_clean(number=0):
    """ Cleans up old archives. """
    number = int(number) if int(number) > 0 else 1
    local(f"ls -t versions/*.tgz | tail -n +{number + 1} | xargs rm -f")
    run(f"ls -t /data/web_static/releases/ | tail -n +{number + 1} | \
         xargs -I {{}} rm -rf /data/web_static/releases/{{}}")
