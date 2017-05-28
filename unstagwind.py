#!/usr/bin/python

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

#file
rawWRF = 'wrfout_d01_2017-04-01_00:00:00'

#######################
#read raw data session#
#######################

dsetWRF = Dataset(rawWRF, mode = 'r')

#	float U(Time, bottom_top, south_north, west_east_stag) ;
#		U:FieldType = 104 ;
#		U:MemoryOrder = "XYZ" ;
#		U:description = "x-wind component" ;
#		U:units = "m s-1" ;
#		U:stagger = "X" ;
#		U:coordinates = "XLONG_U XLAT_U XTIME" ;
zonalwind = dsetWRF.variables['U'][:]

#	float V(Time, bottom_top, south_north_stag, west_east) ;
#		V:FieldType = 104 ;
#		V:MemoryOrder = "XYZ" ;
#		V:description = "y-wind component" ;
#		V:units = "m s-1" ;
#		V:stagger = "Y" ;
meridwind = dsetWRF.variables['V'][:]

###################
#calculate session#
###################

tmhor, bthor, snhorstag, wehor =  np.shape(meridwind)
tmver, btver, snver, weverstag = np.shape(zonalwind)
zonalunstag = np.zeros((tmhor,bthor,snver,wehor))
meridunstag = np.zeros((tmhor,bthor,snver,wehor))

#interpolate zonal wind
for i in xrange(wehor):
	zonalunstag[:,:,:,i] = (zonalwind[:,:,:,i] + zonalwind[:,:,:,i+1]) / 2.0

#interpolate meridional wind
for i in xrange(snver):
	meridunstag[:,:,i,:] = (meridwind[:,:,i,:] + meridwind[:,:,i+1,:]) / 2.0

wind = (zonalunstag**2.0 + meridunstag**2.0)**0.5
print wind
print
print np.shape(wind)
