#!/usr/bin/env python
#coding:utf-8

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.108', 22, 'alex', '123')
stdin, stdout, stderr = ssh.exec_command('df')
print stdout.read()
ssh.close();