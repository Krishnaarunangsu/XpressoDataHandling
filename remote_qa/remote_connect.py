import paramiko
from subprocess import Popen, PIPE
import time

import paramiko
import pexpect
import pytest

from . import environment
from . import loggers
from . import sshtun
from .switch_general import SwitchGeneral, SwitchReal
from .xmlrpc_proxy import TimeoutServerProxy as xmlrpcProxy
from .custom_exceptions import SwitchException


class RemoteConnectSSH:
    def __init__(self, ip_address, _sshtun_port, ssh_user, ssh_user_pass):
        """
        Initialization

        Args:
            ip_address:
            port:
            ssh_user:
            ssh_user_pass:

        Return:

        """
        self.ip_address = ip_address
        self._sshtun_port = _sshtun_port
        self.ssh_user = ssh_user
        self.ssh_user_pass = ssh_user_pass


    def execute_ssh_command(self, command):
        """
        Executes command on switch.
        Args:
            command(str):  ssh command to execute
        :return:
        """
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Make connection and create shell.
        client.connect(self.ip_address, self._sshtun_port, self.ssh_user, self.ssh_user_pass)
        shell = client.invoke_shell()

        # Execute command and get results.
        _, stdout, stderr = client.exec_command(command)
        data = self._read_command_output(stdout, stderr, 'both')

        # Close connection.
        shell.close()
        client.close()

        return data

    def _read_command_output(self, stdout, stderr, ret_mode):
        """Read result of not-interactive command execution.
        Args:
            stdout(str):  StdOut info
            stderr(str):  StdErr info

        Return:
        ret_mode(str):  return mode. both|stderr|stdout
        """
        if ret_mode.lower() == 'both':
            return stdout.read(), stderr.read()
        elif ret_mode.lower() == 'stderr':
            return stderr.read()
        else:
            return stdout.read()

    def copy_file(hostname, port, username, password, src, dst):
        """
        Args:
            hostname
            port:
            username:
            password:
            src:
            dst:

        Return:

        """
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        print (" Connecting to %s \n with username=%s... \n" %(hostname,username))
        t = paramiko.Transport(hostname, port)
        t.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        print ("Copying file: %s to path: %s" %(src, dst))
        sftp.put(src, dst)
        sftp.close()
        t.close()



# https://www.programcreek.com/python/example/4561/paramiko.SSHClient
# https://github.com/paramiko/paramiko/issues/629
