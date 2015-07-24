#!/usr/bin/python
#-*-coding:utf8-*-
__author__ = 'iscalik'

import pexpect,time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ip')
parser.add_argument('username')
parser.add_argument('password')
args = parser.parse_args()
child = pexpect.spawn('telnet ' + args.ip);
child.expect('Escape.*');
child.sendline(args.username);
child.sendline(args.password); # sifre yoksa child.sendline(""); olarak degistirin.
time.sleep(5)
child.sendline('set reboot');
child.sendline('exit');
child.expect(pexpect.EOF);
print child.before;
