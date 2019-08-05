from fabric.api import run, env, local
from os import path
import re

def hello():
    """

    :return:
    """
    print('Hello')
    run('hostname')

def save():
    """
    Args:

    Return:

    :return:
    """
    s = 1+2
    print(s)

def ls():
    output = local('dir')


env.roledefs = {
'web': ['172.16.12.1', '172.16.12.2', '172.16.12.3',],
'media': ['172.16.12.4',],
'staging': ['172.16.12.5',],
'testing': ['192.168.56.3',],
'database': ['172.16.12.7', '172.16.12.8',],
}
env.site_list = []
env.root_path = '/var/websites'


### Setup environments
def testing(site=None):
    env.hosts = env.roledefs['testing']
    env.user = 'coordt'
    if site:
        get_site_list(site)


def staging(site=None):
    env.hosts = env.roledefs['staging']
    env.user = 'staginguser'
    if site:
        get_site_list(site)


def production(site=None):
    env.hosts = env.roledefs['web']
    env.user = 'produser'
    if site:
        get_site_list(site)


def get_site_list(site=None):
    if not site:
        site = input('Please specify which site (a comma delimited list is accepted:')
    if isinstance(site, (tuple, list)):
        env.site_list = site
    else:
        env.site_list = site.split(',')

def validate_input():
    user_name = '1'  #something that doesn't validate
    while not re.match("^[A-Za-z]*$", user_name):
        user_name = input("Please enter your name: ")
        print ("Error! Make sure you only use letters in your name")
    else:
        print("Hello! "+ user_name)
    return user_name

### Host Tasks
def check_host():
    """
    Check that the host has all the required commands installed
    """
    local("echo Checking for required commands")
    required_commands = ['wget', 'python', 'tar', 'gzip', 'hg', 'sudo', 'chown',
                        'chmod', 'patch', 'grep',]
    for command in required_commands:
        run('which %s' % command)

def install_package(package):
    """
    Install a package on a host using apt-get
    """

# hello()
save()
ls()


#  https://stackoverflow.com/questions/33881152/validate-user-input-using-regular-expressions
#  https://pythonspot.com/regular-expressions/
