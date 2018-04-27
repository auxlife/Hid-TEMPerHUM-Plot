#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

tempdata = []
humdata = []
dates = []
# Read the data from db
con = mdb.connectcon = ('DBHOST', 'DBUSER', 'DMPASS', 'DB');
cur = con.cursor()
cur.execute("SELECT datetime, temp, hum  FROM readings WHERE (HOUR(datetime)=0 OR HOUR(datetime) = 12) AND (MINUTE(datetime)=0 OR MINUTE(datetime)=15)")
for i in range(cur.rowcount):
        row = cur.fetchone()
        date = matplotlib.dates.date2num(row[0])
        dates.append(date)
        tempdata.append(row[1])
		humdata.append(row[2])
con.close()

fig, ax = plt.subplots(figsize=(6,5))
ax2 = ax.twinx()
ax.plot_date( dates, tempdata, fmt='-')
ax2.plot_date(dates, humdata,'r-')
temp_mean = [np.mean(tempdata)]*len(dates)
ax.plot(dates,temp_mean, linestyle='--')
ax.xaxis.set_major_formatter(DateFormatter('%m/%d/%y'))

ax.set_ylabel('Temperature F')
ax2.set_ylabel('RH %')
for label in ax.get_xticklabels():
    label.set_rotation(60)
plt.tight_layout()

plt.savefig('/var/www/html/alltemp.png')
