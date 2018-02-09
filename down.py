from ftplib import FTP 
import os
ftp_addr='ftp.airnowapi.org'
f=FTP(ftp_addr)

user='SPATIAL'
password="PB13204062"
f.login(user,password)
print f.getwelcome()
f.cwd("GRIB2")
bufsize=1024
filename="US-18012515_pm25.grib2"
file_handle=open(filename,"wb").write
f.retrbinary('RETR %s' % os.path.basename(filename),file_handle,bufsize)
print "success"
f.quit