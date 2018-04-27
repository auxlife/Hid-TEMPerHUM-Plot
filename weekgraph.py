#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import matplotlib
import numpy as np

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

tempdata = []
humdata = []
dates = []
# Read the data from db
con = mdb.connectcon = ('DBHOST', 'DBUSER', 'DMPASS', 'DB');
cur = con.cursor()
cur.execute("SELECT datetime, temp, hum  FROM readings WHERE datetime BETWEEN DATE_SUB(NOW(), INTERVAL 7 DAY)  AND NOW()")

for i in range(cur.rowcount):
        row = cur.fetchone()
        date = matplotlib.dates.date2num(row[0])
        dates.append(date)
        tempdata.append(row[1])
		humdata.append(row[2])
con.close()

fig, ax = plt.subplots(figsize=(15,5))
ax2 = ax.twinx()
ax.plot_date(dates, tempdata, fmt='-',)
ax2.plot_date(dates, humdata,'r-')
temp_mean = [np.mean(tempdata)]*len(dates)
ax.plot(dates,temp_mean, linestyle='-')

ax.set_ylabel('Temperature F')
ax2.set_ylabel('RH %')
for label in ax.get_xticklabels():
    label.set_rotation(60)
plt.tight_layout()

plt.savefig('/var/www/html/weektemp.png')
