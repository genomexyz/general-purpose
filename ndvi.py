#!/usr/bin/python

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

#setting
clearthreshold = 296.0

#file
rawB03name = 'H08_B03_Indonesia_201706090500.nc'
rawB04name = 'H08_B04_Indonesia_201706090500.nc'
rawB13name = 'H08_B13_Indonesia_201706090500.nc'


#######################
#read raw data session#
#######################

dsetB03 = Dataset(rawB03name, mode = 'r')
dsetB04 = Dataset(rawB04name, mode = 'r')
dsetB13 = Dataset(rawB13name, mode = 'r')

#get lat and lon
lat = dsetB03.variables['latitude'][:]
lon = dsetB03.variables['longitude'][:]

#get data
B03 = dsetB03.variables['VS'][0]
B04 = dsetB04.variables['N1'][0]
B13 = dsetB13.variables['IR'][0]

###################
#calculate session#
###################

#to calculate NDVI = (B11 - B08) / (B11 + B08)
#to calculate EVI = (B11 - B08) / (B11 + 6 * B08 - 7.5 * B07 + 1)

NDVI = (B04 - B03) / (B04 + B03)
NDVI[NDVI < 0.2] = np.nan
B13[B13 < clearthreshold] = np.nan
#NDVI = np.ma.masked_invalid(np.atleast_2d(NDVI))
NDVI = np.ma.masked_where(np.isnan(NDVI),NDVI)
#NDVI = np.ma.masked_where(np.isnan(B13),NDVI)

print NDVI
###############
#plotting time#
###############

m = Basemap(resolution='l', projection='merc', \
llcrnrlon=90, llcrnrlat=-20, urcrnrlon=149, urcrnrlat=20) #for mercator

#draw map coastline, etc
m.drawcoastlines(linewidth=0.75)
m.drawcountries(linewidth=0.75)

#make our lon and lat 2D
lon1, lat1 = np.meshgrid(lon, lat)

#for NDVI
plt.title('NDVI')
cs = m.pcolormesh(lon1, lat1, np.squeeze(NDVI), cmap='coolwarm', latlon=True)
cbar = m.colorbar(cs, location='bottom', pad="10%") #add color bar
plt.show()
