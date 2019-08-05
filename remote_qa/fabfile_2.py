from fabric.api import run, env, local
from os import path
import re


env.roledefs = {
'testing': ['172.16.3.1','172.16.3.2'],
}

env.root_path = '/home/xprops'


### Setup environments
def testing(site=None):
    env.hosts = env.roledefs['testing']
    env.user = 'xprops'
    return env.hosts, env.user


### Host Tasks
def check_host():
    """
    Check that the host has all the required commands installed
    """
    print(testing())
    local("echo Checking for required commands")
    required_commands = ['wget', 'python', 'tar', 'gzip', 'hg', 'sudo', 'chown',
                        'chmod', 'patch', 'grep',]
    for command in required_commands:
        run('which %s' % command)

check_host()
