#!/usr/bin/python

import pycurl
import datetime
import time
import os

#bmkg satellite data archiver

#for algorithm sake
counter = 0
check_time = 100

#list of address
addr = ['http://satelit.bmkg.go.id/IMAGE/HIMA/H08_EH_Indonesia.png', \
'http://satelit.bmkg.go.id/IMAGE/HCAI/CLC/HCAI_CLC_Indonesia.png', \
'http://satelit.bmkg.go.id/IMAGE/HIMA/H08_RP_Indonesia.png', \
'http://satelit.bmkg.go.id/IMAGE/MTS/VS/MTS_VS_Indonesia.png', \
'http://satelit.bmkg.go.id/IMAGE/HIMA/H08_WE_Indonesia.png', \
'http://satelit.bmkg.go.id/IMAGE/MTS/IW/MTS_IW_Indonesia.png', \
'http://satelit.bmkg.go.id/IMAGE/HIMA/H08_EH_Jakarta.png', \
'http://satelit.bmkg.go.id/IMAGE/HIMA/H08_NC_Indonesia.png', \
'http://satelit.bmkg.go.id/Trajektori/Asap.PNG', \
'http://satelit.bmkg.go.id/IMAGE/FY2/ENH/FY2G_ENH_BBS.png', \
'http://satelit.bmkg.go.id/IMAGE/FY2/ENH/FY2G_ENH_BBU.png', \
'http://satelit.bmkg.go.id/IMAGE/FY2/ENH/FY2G_ENH_Indonesia.png', \
'http://satelit.bmkg.go.id/IMAGE/FY2/ENH/FY2E_ENH_BBS.png', \
'http://satelit.bmkg.go.id/IMAGE/FY2/ENH/FY2E_ENH_BBU.png', \
'http://satelit.bmkg.go.id/IMAGE/FY2/ENH/FY2E_ENH_Indonesia.png']

name = ['citra_satelit_indonesia', 'citra_jenis_awan_indonesia', \
'potensi_hujan_indonesia', 'citra_satelit_VIS', 'citra_satelit_IR3_WV', \
'vektor_angin', 'citra_satelit_jabodetabek', 'citra_satelit_natural_color_indonesia', \
'citra_sebaran_asap', 'Fengyun_2G_BBS', 'Fengyun_2G_BBU', 'Fengyun_2G_Indonesia', \
'Fengyun_2E_BBS', 'Fengyun_2E_BBU', 'Fengyun_2E_Indonesia']

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

while True:
	print 'time to download data'
	yearr = datetime.datetime.utcnow().strftime("%Y")
	monthh = datetime.datetime.utcnow().strftime("%m")
	day = datetime.datetime.utcnow().strftime("%H")
	hour = datetime.datetime.utcnow().strftime("%H")
	minute = datetime.datetime.utcnow().strftime("%M")

	minuteint = int(minute) / 10	#we will manipulate this for loop sake

	if check_time != minuteint:
		for add in addr:

			try:
				os.makedirs(yearr)
			except OSError:
				pass

			try:
				os.makedirs(yearr+'/'+monthh)
			except OSError:
				pass

			#manipulate minute
			resmin = str(minuteint)+"0"

			#concat time
			conctime = hour+resmin
			
			#outputname
			outname = name[counter]+'_'+yearr+monthh+day+conctime+'.png'
			
			#download now
			download(add, (yearr+"/"+monthh+'/'+outname))
			counter += 1
			print 'download success'
		check_time = minuteint
		counter = 0
	time.sleep(60) #looping every 1 minutes
