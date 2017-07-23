#!/usr/bin/python
import argparse
import paramiko
import sys
import os
import select
import threading
import time


def run_cmd(ip, cmd, username=None, password=None):
    if username is None:
        username = 'root'
    if password is None:
        password = "changeme"
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, password)
        print "Connected to %s" % ip
        # Send the command (non-blocking)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # Wait for the command to terminate
        while not stdout.channel.exit_status_ready():
            # Only print data if there is data to read in the channel
            if stdout.channel.recv_ready():
                rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
                if (len(rl) > 0):
                    # Print data from stdout
                    print stdout.channel.recv(1024)
        print "Command done, closing SSH connection"
    except paramiko.AuthenticationException:
        print "Authentication failed when connecting to %s" % ip
        sys.exit(1)
        # except:
        #   print "Could not SSH to %s, waiting for it to start" % ip
        ssh.close()
    return


def main():
    parser = argparse.ArgumentParser(description="This is out Description")
    parser.add_argument('--ip', type=str, help="IP address is required", required=True)
    parser.add_argument('--cmd', type=str, help="Type Command you want to run to remote system", required=True)
    parser.add_argument('--user', type=str, help="User Name  is required", required=False)
    parser.add_argument('--password', type=str, help="Password Please", required=False)
    parser.add_argument('-o', type=str, help="This is Optional", required=False)
    cmd_argu = parser.parse_args()
    ipvar = cmd_argu.ip
    cmdvar = cmd_argu.cmd
    user = cmd_argu.user
    passs = cmd_argu.password
    # print(type(ipvar),type(cmdvar))
    print 'Following Cmd {0} runing on {1} System'.format(cmdvar, ipvar)
    run_cmd(ipvar, cmdvar, user, passs)


if __name__ == '__main__':
    main()
