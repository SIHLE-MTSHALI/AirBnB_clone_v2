#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""
from fabric.api import *

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """Cleans up old archives."""
    number = int(number) if int(number) > 0 else 1
    local(f"ls -tr versions/*.tgz | head -n -{number} | xargs rm -rf")
    run(f"ls -tr /data/web_static/releases/ | head -n -{number} | \
         xargs -I {{}} rm -rf /data/web_static/releases/{{}}")
