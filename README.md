# Hid-TEMPerHUM-Plot
Read/Store/View Temp/Hum readings from TEMPerHum v3.1 (SIENOC TEMPerHUM, white internal sensor, blue TXT button, TEMPerX_V3.1, HID ID 413d:2107)

cronjobs - entries to add to scheduler to take readings and to update graph images

readings.sql - table structure

hr/day/week/month/allgraph.py - scripts to read db and creat png images to save in /var/www/html/

readtemp.py - executes precompiled hid-query application (https://github.com/edorfaus/TEMPered/blob/master/utils/hid-query.c) and inserts into db while saving reading to a log file

www/index.html - simple html file to load precreated images for users
