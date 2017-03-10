#!/usr/bin/python

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt


sample = '/home/genomexyz/prjsatandro/tes1.nc'
fh = Dataset(sample, mode = 'r')
cmaping = colors.ListedColormap(['r','g','b'])

#print(fh.dimensions.keys())
#print(fh.variables.keys())

#print(fh.variables['WV'].units)
plotvar = fh.variables['WV']	 #composition: time, latitude, longitude
lat = fh.variables['latitude']	#grid 0,0 is bottom left and max,max is upper right
lon = fh.variables['longitude']	#grid resolution is 0.02 degree
#plotvar2 = fh.variables['longitude'][:]


#print plotvar
#print plotvar2

#m = Basemap(width=5000000, height=3500000, resolution='l', projection='merc',\
#lat_ts=40, lat_0=lat_0, lon_0=lon_0)

m = Basemap(resolution='l', projection='merc', \
llcrnrlon=90, llcrnrlat=-20, urcrnrlon=149, urcrnrlat=20) #for mercator

#draw map coastline, etc
m.drawcoastlines(linewidth=0.25)
m.drawcountries(linewidth=0.25)
#m.fillcontinents(color='coral',lake_color='aqua')
#m.drawmapboundary(fill_color='aqua')

#make our lon and lat 2D
lon1, lat1 = np.meshgrid(lon, lat) #lon1 nilai array 1d berulang mendatan lat1 berulang vertikal dimensinya lon1 x lat1

print np.size(lon1)
print np.size(lat1)
print 

print 'lintangnya', fh.variables['longitude'][:]
print plotvar
print fh.variables['WV']
print np.size(np.squeeze(plotvar))
plt.title('WV yang terdeteksi (tester)')
cs = m.pcolormesh(lon1, lat1, np.squeeze(plotvar), cmap='coolwarm', latlon=True)
cbar = m.colorbar(cs, location='bottom', pad="10%") #add color bar
plt.show()

#llcrnrlon	longitude of lower left hand corner of the desired map domain (degrees).
#llcrnrlat	latitude of lower left hand corner of the desired map domain (degrees).
#urcrnrlon	longitude of upper right hand corner of the desired map domain (degrees).
#urcrnrlat	latitude of upper right hand corner of the desired map domain (degrees).
