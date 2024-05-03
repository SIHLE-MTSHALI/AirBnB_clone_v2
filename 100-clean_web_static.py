#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""
from fabric.api import env, local, run

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 0:
        return False

    number = 1 if number == 0 else number + 1

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
