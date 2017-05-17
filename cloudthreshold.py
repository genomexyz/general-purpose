#!/usr/bin/python

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

def detkindcloud(under, upper, data):
	Y, X = np.shape(data)
	cloudmat = np.zeros((Y, X), dtype = np.int)
	cloudmat[data < upper] = 1
	cloudmat[data < under] = 0
	return cloudmat

def detclear(upper, data):
	Y, X = np.shape(data)
	cloudmat = np.zeros((Y, X), dtype = np.int)
	cloudmat[data > upper] = 1
	return cloudmat


#setting
rawdataname = 'IR1.nc'
CBthreshold = 233
highthreshold = 252
middlethreshold = 272
lowthreshold = 286
clearthreshold = 298

#######################
#read raw data session#
#######################

dset = Dataset(rawdataname, mode = 'r')

plotvar = dset.variables['IR']
lat = dset.variables['latitude']	#grid 0,0 is bottom left and max,max is upper right
lon = dset.variables['longitude']


########################
#detect all kind of cloud#
########################

CB = detkindcloud(0, 233, plotvar[0])
highcloud = detkindcloud(CBthreshold, highthreshold, plotvar[0])
middlecloud = detkindcloud(highthreshold, middlethreshold, plotvar[0])
lowcloud = detkindcloud(middlethreshold, lowthreshold, plotvar[0])
clearcloud = detclear(lowthreshold, plotvar[0])

#print np.sum(CB)
#print np.sum(highcloud)
#print np.sum(middlecloud)
#print np.sum(lowcloud)
#print np.sum(clearcloud)

###############
#plotting time#
###############

lev = [.99,2]
collow = ['orange']
colhigh = ['cyan']
colmid = ['yellow']
colcb = ['red']
colclear = ['black']

m = Basemap(resolution='i',llcrnrlon=90, llcrnrlat=-15, urcrnrlon=150,urcrnrlat=15)


#plotting cloud with contourf
x,y = np.meshgrid(np.linspace(lon[0],lon[-1],len(plotvar[0,0,:])), np.linspace(lat[0],lat[-1],len(plotvar[0])))
pltcb = m.contourf(x,y,CB,levels=lev,colors=colcb,labels='Awan CB')
pltlc = m.contourf(x,y,lowcloud,levels=lev,colors=collow,labels='Low Cloud')
pltmc = m.contourf(x,y,middlecloud,levels=lev,colors=colmid,labels='Middle Cloud')
plthc = m.contourf(x,y,highcloud,levels=lev,colors=colhigh,labels='High Cloud')
pltclr = m.contourf(x,y,clearcloud,levels=lev,colors=colclear,labels='Clear')


#draw map coastline, etc
m.drawcoastlines(linewidth=0.75, color = 'blue')
m.drawcountries(linewidth=0.75, color = 'blue')


#plt.legend(handles = [pltcb, pltlc, pltmc, plthc, pltclr])
#plt.colorbar(pltcb)
print lev
#plt.colorbar(ticks = lev)
plt.show()

