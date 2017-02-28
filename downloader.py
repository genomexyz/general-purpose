#!/usr/bin/python

import pycurl
import datetime
import time
import os

#code to download infrared data

formatweb = "http://www.data.jma.go.jp/mscweb/data/himawari/img/se3/se3_b13_"
typefile = "ifr"

def download (alamat, outp):
	with open(outp, 'wb') as f:
		c = pycurl.Curl()
		c.setopt(c.URL, alamat)
		c.setopt(c.WRITEDATA, f)
		c.perform()
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

	minuteint = int(minute)	#we will manipulate this for loop sake
	
	try:
		os.makedirs(typefile)
	except OSError:
		pass

	try:
		os.makedirs(typefile+"/"+yearr)
	except OSError:
		pass	

	try:
		os.makedirs(typefile+"/"+yearr+"/"+monthh)
	except OSError:
		pass

	#manipulate minute
	roundmin = minuteint / 10
	resmin = str(roundmin)+"0"

	#concat time
	conctime = hour+resmin

	#get the url
	urlweb = formatweb+conctime+".jpg"
	download(urlweb, (typefile+'/'+yearr+'/'+monthh+'/'+yearr+monthh+day+conctime+'.jpg'))
	time.sleep(600) #looping every 10 minutes
