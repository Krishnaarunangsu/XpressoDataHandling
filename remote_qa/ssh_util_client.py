import paramiko
import socket


print(f'Localhost Info:\n{socket.getaddrinfo("localhost", 8080)}')

ssh = paramiko.SSHClient()
print(ssh)



client = paramiko.SSHClient()
print(client)
print(client.load_system_host_keys())
client.connect('uswv-uinq12003-001')
stdin, stdout, stderr = client.exec_command('ls -l')

# result = ssh.connect('uswv-uinq12003-001',port=22, username='xprops', password='abz00ba1nc')
# print(result)

#stdin, stdout, stderr = ssh.exec_command('pwd')
# stdin, stdout, stderr = ssh.exec_command('sudo python /home/path/remote_test.py')



#  http://docs.paramiko.org/en/2.6/api/client.html
