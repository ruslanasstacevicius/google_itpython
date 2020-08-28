#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
import emails

def check_disk_usage():
    du = shutil.disk_usage("/")
    free = du.free / du.total * 100
    return free > 20

def check_ram_usage():
    avail = psutil.virtual_memory().available
    remain = avail / (1024**2)
    return remain > 500

def check_cpu_usage():
    cpupc = psutil.cpu_percent(1)
    return cpupc < 80

def check_localhost():
    lh = socket.gethostbyname('localhost')
    return lh == '127.0.0.1'

functions_messages = [
        (check_disk_usage, 'Error - Available disk space is less than 20%'),
        (check_ram_usage, 'Error - Available memory is less than 500MB'),
        (check_cpu_usage, 'Error - CPU usage is over 80%'),
        (check_localhost, 'Error - localhost cannot be resolved to 127.0.0.1')
        ]

user = os.getenv('USER')
body_text = 'Please check your system and resolve issue as soon as possible'

for f, subj in functions_messages:
    print("checking:", f.__name__)
    if not f():
        print(subj)
        email = emails.generate('automation@example.com', user + '@example.com', subj, body_text ,'')
        emails.send(email)

