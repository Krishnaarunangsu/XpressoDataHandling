import paramiko



def get_hostname_by_ssh(host_ip):
    '''
    Make a connection to the remote system and get its hostname
    '''
    print('Checking out {}'.format(host_ip))
    ssh = paramiko.SSHClient()
    print(f'SSH:{ssh}')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host_ip,
                username='xprops',
                password='abz00ba1nc')
    _, stdout, _ = ssh.exec_command('hostname')
    hostname = stdout.read()
    print(f'HostName:\n{hostname}')
    get_out_put(hostname)
    # stdin, stdout, stderr = ssh.exec_command('pwd')
    # print(stdin)
    # print(stdout)
    ssh.close()
    if isinstance(hostname, bytes):
        hostname = hostname.decode('utf-8')
    print('Found {}'.format(hostname.strip()))
    return hostname.strip()


def get_out_put(hostname):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(hostname)
    c = client.connect(hostname = 'uswv-uinq12003-001', username='xprops', password='abz00ba1nc')
    print(c)

    stdin, stdout, stderr = client.exec_command('ls -l')

    for line in stdout:
        print(line.strip('\n'))
    client.close()

get_hostname_by_ssh('172.16.3.1')
