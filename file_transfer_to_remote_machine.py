from paramiko import SSHClient, sftp, SFTPClient, AutoAddPolicy, util
from scp import SCPClient
import os


def file_transfer(remote_ip, username, password, source_directory,
                  destination_directory, shell_command=None, PWD=None, cmd=None):
    PROFILE = ". /etc/profile 2&>/dev/null;. ~/.bash_profile 2&>/dev/null;" \
              ". /etc/bashrc 2&>/dev/null;. ~/.bashrc 2&>/dev/null;"
    PATH = "export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin;"
    ssh = SSHClient()
    util.log_to_file("paramico_file_transfer.txt")
    ssh.set_missing_host_key_policy(AutoAddPolicy)
    ssh.load_system_host_keys()
    ssh.connect(remote_ip, username=username, password=password)
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(files=source_directory, remote_path=destination_directory, recursive=True)
        # scp.get('/home/marjan/Pictures/pic.png')
        stdin, stdout, stderr = ssh.exec_command(shell_command)
        # env_stdin, env_stdout, env_stderr = ssh.exec_command(PROFILE + PWD + PATH + cmd)
        for line in stdout:
            print('... ' + line.strip('\n'))
       # sftp.put(source_directory, destination_directory, callback=file_transfer)
        error = stderr.read()
        print(error)
        print(os.getcwd())
    ssh.close()
    scp.close()


if __name__ == "__main__":
    file_transfer('192.168.2.80', 'marjan', 'ma',
                  '/home/marjan/Desktop/', '/home/marjan/Pictures/hello',
                  'cd /home/marjan/Pictures/hello/; ls'
                  )
