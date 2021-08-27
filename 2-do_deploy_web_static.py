#!/usr/bin/python3
''' Fabric script that generates a .tgz archive '''

from fabric.api import *
from datetime import datetime

env.hosts = [
    '35.231.143.58',
    '35.185.49.2'
]
env.user = "ubuntu"


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder'''
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_"+date+".tgz web_static")
        return ("versions/web_static_"+date+".tgz")
    except:
        return (None)


def do_deploy(archive_path):
    ''' distributes an archive to my web servers '''
    if (not archive_path):
        return (False)

    try:
        put(archive_path, '/tmp')
        folder_path = "/data/web_static/releases/"+archive_path[9:-4]
        run("mkdir -p " + folder_path)
        run("tar zxvf /tmp/" + archive_path[9:] + " -C " + folder_path)
        run("mv " + folder_path + "/web_static/* " + folder_path)
        run("rm -rf " + folder_path + "/web_static/")
        run("rm -rf /tmp/" + archive_path[9:])
        run("rm /data/web_static/current")
        run("ln -sf " + folder_path + " /data/web_static/current")
        return (True)
    except:
        return (False)
