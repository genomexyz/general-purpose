#!/usr/bin/python

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, interp
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import datetime

def create_grid_output(inputx, inputy, magnificent):
	dimx = np.asarray(inputx[0].shape)
	dimy = np.asarray(inputy[:,0].shape)
	outx = np.linspace(inputx[0, 0], inputx[0, -1], dimx[0] * magnificent)
	outy = np.linspace(inputy[0, 0], inputy[-1, 0], dimy[0] * magnificent)
	return np.meshgrid(outx, outy)	#order of return: x-dimension, y-dimension

namefilein = '/home/genomexyz/prjsatandro/tes1.nc'
namefileout = '/home/genomexyz/keluaran.nc'
var = 'WV'
formatfile = 'NETCDF4'

#open data
fh = Dataset(namefilein, mode = 'r')

#extract variable in data
plotvar = fh.variables[var][0, 710:1096, 1395:1772]	#composition: time, latitude, longitude
lat = fh.variables['latitude'][710:1096]	#grid 0,0 is bottom left and max,max is upper right
lon = fh.variables['longitude'][1395:1772]	#grid resolution is 0.02 degree

#prepare input grid
lon1, lat1 = np.meshgrid(lon, lat)
m = Basemap(resolution='l', projection='merc', \
llcrnrlon=117.9, llcrnrlat=-5.8, urcrnrlon=125.45, urcrnrlat=1.92)	#for mercator
x, y = m(lon1, lat1)												#grid input

#create grid output
x1, y1 = create_grid_output(x, y, 2)

#interpolation
dataout = interp(plotvar, x[0], y[:,0], x1, y1)

#re-create lon lat
lonnew, latnew = m(x1, y1, inverse=True)


print np.size(x1[0]), np.size(y1[:,0])
print np.size(x[0]), np.size(y[:,0])
###################
#re-create nc file#
###################

#init, create dimension
createncfile = Dataset(namefileout, 'w', format=formatfile)
timex = createncfile.createDimension('time')
latss = createncfile.createDimension('latitude')
lonss = createncfile.createDimension('longitude')

#create variable
times = createncfile.createVariable('time', np.int32, ('time',))
latitudes = createncfile.createVariable('latitude', np.float64, ('latitude',))
longitudes = createncfile.createVariable('longitude', np.float64, ('longitude',))
WVs = createncfile.createVariable('WV', np.float64, ('time','latitude','longitude'))

#set attribute
createncfile.description = 'example interpolation'
createncfile.history = 'Created ' + datetime.datetime.utcnow().strftime("%H")
createncfile.source = 'eksperimen pertama'

#set variable unit
latitudes.units = 'degree_north'
longitudes.units = 'degree_east'
WVs.units = 'entah'

#write data
latitudes[:] = latnew[:,0]
longitudes[:] = lonnew[0]
times[:] = 1
WVs[0, 0:np.size(latnew[:,0]), 0:np.size(lonnew[0])] = dataout
