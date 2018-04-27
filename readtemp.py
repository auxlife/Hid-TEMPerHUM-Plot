#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import commands
import os
import sys
import datetime

logfile = '/var/log/temphum.log'
errfile = '/var/log/temphum.err'
hidpath = '/dev/hidraw#'
pypath = os.path.dirname(os.path.realpath(sys.argv[0]))

if os.path.exists(logfile):
        openmethod = 'a'
else:
        openmethod = 'w'
logfile = open(logfile, openmethod)

if os.path.exists(errfile):
        openmethod = 'a'
else:
        openmethod = 'w'
errfile = open(errfile, openmethod)


output = commands.getoutput(pypath + '/hid-query ' + hidpath + ' 0x01 0x80 0x33 0x01 0x00 0x00 0x00 0x00').splitlines()[6].split()
ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
temp = str(((((int(output[2],16) << 8) + int(output[3],16))/100)*1.8 +32))
hum = str((((int(output[4],16) << 8) + int(output[5],16))/100))
output = ts+' '+temp+'F '+hum+'%\n';

try:
    con = mdb.connect('DBHOST', 'DBUSER', 'DMPASS', 'DB');
    cur = con.cursor()
    sql = "INSERT INTO `readings` (`ID`, `datetime`, `temp`, `hum`) VALUES (NULL, '" + ts +"', '"+temp+"', '"+hum+"')"


    cur.execute(sql)
    con.commit()
    logfile.write(output)
except mdb.Error, e:

    print "Error %d: %s" % (e.args[0],e.args[1])
    errfile.write(output)
    sys.exit(1)

finally:

    if con:
        con.close()


errfile.close()
logfile.close()