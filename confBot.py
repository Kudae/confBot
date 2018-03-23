# log in to someone's machine and change
import paramiko

# connection variables
port = 22

# login variables
username = "admin"
password = "vpn123"

# actions over ssh
command= "hostname"

# print("\n")
# print("Using username: {}\n" .format(username))
# print("Using password: {}\n" .format(password))
# print("Using port: {}\n" .format(port))

# SSH connection function
def conn():
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())

        client.connect(hostname, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read()),

    finally:
        client.close()

    # run through ip address range and connecto to devices
    for x in range(251):
        hostname = "172.25.84.{2}" .format(x)
        print(hostname)
        conn(hostname,username,password,command)
