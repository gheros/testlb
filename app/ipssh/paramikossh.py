import paramiko

# t = paramiko.Transport(("172.16.20.120", "端口"))
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("172.16.60.120",22,"root", "34shidai")
stdin, stdout, stderr = ssh.exec_command("ls")
print (stdout.readlines())
ssh.close()