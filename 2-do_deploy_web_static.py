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
        put(archive_path, "/tmp")
        file_name = archive_path[9:]
        release_name = file_name[:-4]
        release_folder = "/data/web_static/releases/" + release_name
        run("mkdir -p " + release_folder)
        run("tar zxvf /tmp/" + file_name + " -C " + release_folder)
        run("mv " + release_folder + "/web_static/* " + release_folder)
        run("rm -rf " + release_folder + "/web_static/")
        run("rm -rf /tmp/" + file_name)
        run("rm /data/web_static/current")
        run("ln -sf " + release_folder + " /data/web_static/current")
        return (True)
    except:
        return (False)
