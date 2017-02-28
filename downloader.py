#!/usr/bin/python

import pycurl
import datetime
import time
import os

check_time = 100	#algorithm sake

#formatweb = "http://www.data.jma.go.jp/mscweb/data/himawari/img/se3/se3_b13_"
formatweb = "http://www.data.jma.go.jp/mscweb/data/himawari/img/"
typefile = "ifr"

#list of area
area = ['fd_', 'aus', 'ca1', 'nzl', 'pi1', 'pi2', 'pi3', 'pi4', 'pi5', 'pi6', \
'pi7', 'pi8', 'pi9', 'pia', 'se1', 'se2', 'se3', 'se4', 'ha1', 'ha2', 'ha3', \
'ha4', 'ha5', 'ha6', 'hp1', 'hp2', 'hp3', 'jpn']

#list of type
datatype = ['b13', 'b03', 'b08', 'b07', 'dms', 'ngt', 'dst', 'arm', 'dsl', \
'dnc', 'tre', 'trm', 'cve', 'snd', 'vir', 'irv', 'hrp']

def download (alamat, outp):
	connected = False
	with open(outp, 'wb') as f:
		c = pycurl.Curl()
		c.setopt(c.URL, alamat)
		c.setopt(c.WRITEDATA, f)
		while not connected:	#condition if no internet connection
			try:
				c.perform()
			except:
				print 'no internet connection, try again in 10 seconds'
				time.sleep(10)		#try again in 10 seconds
				pass
			connected = True
		c.close()

#download ('http://www.data.jma.go.jp/mscweb/data/himawari/img/se3/se3_b13_1620.jpg', 'gambarsatelit.jpg')


#time for the real action
while True:
	print 'time to download data'
	yearr = datetime.datetime.utcnow().strftime("%Y")
	monthh = datetime.datetime.utcnow().strftime("%m")
	day = datetime.datetime.utcnow().strftime("%H")
	hour = datetime.datetime.utcnow().strftime("%H")
	minute = datetime.datetime.utcnow().strftime("%M")

	minuteint = int(minute) / 10	#we will manipulate this for loop sake

	if check_time != minuteint:
		for typ in datatype:
			for location in area:
				try:
					os.makedirs(typ)
				except OSError:
					pass
			
				try:
					os.makedirs(typ+'/'+location)
				except OSError:
					pass

				try:
					os.makedirs(typ+'/'+location+"/"+yearr+"/"+monthh)
				except OSError:
					pass

				#manipulate minute
				resmin = str(minuteint)+"0"

				#concat time
				conctime = hour+resmin

				#get the url
				urlweb = formatweb+location+'/'+location+'_'+typ+'_'+conctime+".jpg"
				download(urlweb, (typ+'/'+location+"/"+yearr+"/"+monthh+'/'+yearr+monthh+day+conctime+'.jpg'))
				print 'download success'
	check_time = minuteint
	time.sleep(60) #looping every 1 minutes
