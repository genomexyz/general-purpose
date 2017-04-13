#!/usr/bin/python

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

#hint
#from left to right -> 90 until 150 longitude
#from bottom to top -> -20 until 20 latitude
#llcrnrlon	longitude of lower left hand corner of the desired map domain (degrees).
#llcrnrlat	latitude of lower left hand corner of the desired map domain (degrees).
#urcrnrlon	longitude of upper right hand corner of the desired map domain (degrees).
#urcrnrlat	latitude of upper right hand corner of the desired map domain (degrees).


contoh = colors.Colormap('r', N=1)

#all matrix here is list object
def createbinermat(rightmat, leftmat, treshold):
	right = np.asarray(rightmat)
	left = np.asarray(leftmat)
	y, x = np.shape(right)
	out = np.zeros((y,x), dtype=np.int)
	for i in xrange(y):
		for j in xrange(x):
			if (rightmat[i][j]-leftmat[i][j]) <= treshold:
				out[i][j] = 1
			else:
				out[i][j] = 0
	return out 


#criteria for temperature of cloud: IR1 - IR2 <= 2 K
crit1 = 2
#criteria  for top cloud: IR1 - IR3 <= 3 K
crit2 = 3

rawIR1 = '/home/genomexyz/awancb/IR1.nc'
rawIR2 = '/home/genomexyz/awancb/IR2.nc'
rawIR3 = '/home/genomexyz/awancb/IR3.nc'

#read input
readIR1 = Dataset(rawIR1, mode = 'r')
readIR2 = Dataset(rawIR2, mode = 'r')
readIR3 = Dataset(rawIR3, mode = 'r')

#lat and lon matrix
#all nc file here have a same spatial matrix
lat = readIR1.variables['latitude']	#grid 0,0 is bottom left and max,max is upper right
lon = readIR1.variables['longitude']

#exract data from dataset
matrixIR1 = readIR1.variables['IR'][0]
matrixIR2 = readIR2.variables['I2'][0]
matrixIR3 = readIR3.variables['WV'][0]

#selection based on criteria
matrixcrit1 = createbinermat(matrixIR1, matrixIR2, crit1)
matrixcrit2 = createbinermat(matrixIR1, matrixIR3, crit2)

#detect cb
finalmatrix = matrixcrit1 + matrixcrit2
dimy, dimx = np.shape(finalmatrix)
cb = np.zeros((dimy,dimx), dtype=np.int)
for i in xrange(dimy):
	for j in xrange(dimx):
		if finalmatrix[i][j] == 2:
			cb[i][j] = 1
		else:
			cb[i][j] = 0
#this is necessary!!!
#cb = np.flipud(cb)

#print np.sum(cb)

################
#plotting time!#
################

#make our lon and lat 2D
lon1, lat1 = np.meshgrid(lon, lat)

m = Basemap(resolution='l', projection='merc', \
llcrnrlon=90, llcrnrlat=-20, urcrnrlon=150, urcrnrlat=20) #for mercator

#draw map coastline, etc
m.drawcoastlines(linewidth=0.25)
m.drawcountries(linewidth=0.25)

#finishing
plt.title('Pendeteksi Awan CB ver 1.0')
cs = m.pcolormesh(lon1, lat1, np.squeeze(cb), cmap='Set3', latlon=True)
#cbar = m.colorbar(cs, location='bottom', pad="10%") #add color bar
plt.show()
