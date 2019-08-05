#!/usr/bin/python
from fabric.api import *

env.use_ssh_config = False
env.hosts = ["172.16.3.1"]
env.user = "xprops"
#env.key_filename = "/root/.ssh/id_rsa"
env.password = "abz00ba1nc"
env.port = 22


def uptime():
        print('co')
        run("uptime")
        run ("ls -ltr")


#!/user/bin/env python

# from fabric.api import *

# env.user = 'xprops'
# env.user = 'xprops'
env.user = "xprops"
#env.key_filename = "/root/.ssh/id_rsa"
env.password = "abz00ba1nc"
env.port = 22

env.host = '172.16.3.1'
@task
@hosts("172.16.3.1")
def foo():
        print(env.user)
        print(env.host)
        print('Jagannath')
        run("uptime")
        print('Jagannath')
        run ("ls -ltr")
        print(env.host_string)


#  https://stackoverflow.com/questions/11482859/how-to-force-the-fabric-connect-to-remote-host-before-run-executed
#  https://serversforhackers.com/c/deploying-with-fabric
#  https://github.com/kevin1024/fabric_remote
#  https://www.renatocandido.org/2013/11/using-python-fabric-to-automate-gnulinux-server-configuration-tasks/


foo()
uptime()






