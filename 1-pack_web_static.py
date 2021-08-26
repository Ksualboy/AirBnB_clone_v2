#!/usr/bin/python3
''' Fabric script that generates a .tgz archive '''

from fabric.api import local, env
from datetime import datetime

env.hosts = [
    'ubuntu@35.231.143.58',
    'ubuntu@35.185.49.2'
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
