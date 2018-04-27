#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands
import os
import sys


pypath = os.path.dirname(os.path.realpath(sys.argv[0]))
output = commands.getoutput(pypath + '/hid-query -e').splitlines()
for line in output:
    line = line.split()
    if line[2] == '413d:2107' and line[4] == '1':
        hidpath = line[0]
        break
print("Your hidpath should be set to '" + hidpath+"'")
response = commands.getoutput(pypath + '/hid-query ' + hidpath+" 0x01 0x86 0xff 0x01 0x00 0x00 0x00 0x00").splitlines()
response = response[6].split()+response[8].split()
response = "".join(response).decode("hex").rstrip()

print("Your device responds as: '"+response+"'")
