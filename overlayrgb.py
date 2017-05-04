#!/usr/bin/python

from scipy.misc import imsave
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, interp
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

#rgb = np.zeros((255, 255, 3), dtype=np.uint8)
#rgb[..., 0] = np.arange(255)
#rgb[..., 1] = 1000
#rgb[..., 2] = 1 - np.arange(255)
#imsave('rgb_gradient.png', rgb)
#print rgb[...,0]

#setting
tempmin = 200
tempmax = 330

#input
sampleB03 = 'B03.nc'
sampleB04 = 'B04.nc'
sampleB06 = 'B06.nc'

#extract array
dsetB03 = Dataset(sampleB03, mode = 'r')	#as red
dsetB04 = Dataset(sampleB04, mode = 'r')	#as green
dsetB06 = Dataset(sampleB06, mode = 'r')	#as blue

plotB03 = dsetB03.variables['VS'][0]
plotB04 = dsetB04.variables['N1'][0]
plotB06 = dsetB06.variables['N3'][0]
print np.shape(plotB03)

Y,X = np.shape(plotB03)

rgbnc = np.zeros((Y, X, 3))
rgbnc[..., 0] = plotB03
rgbnc[..., 1] = plotB04
rgbnc[..., 2] = plotB06
rgbnc = np.flipud(rgbnc)
print rgbnc
imsave('rgb_asap.png', rgbnc)
#prepare image matrix MXNX3
