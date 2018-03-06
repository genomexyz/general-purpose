#!/usr/bin/python

import numpy as np
from netCDF4 import Dataset
import csv

#setting
ncfile = 'GRIDONE_2D.nc' #edit ini dan masukkan nama file nc yang ingin dikonversi
ascii3d = 'GRIDONE_2D.xyz' #edit ini dan masukkan nama file keluaran xyz atau teks yang diinginkan

#open nc
dset = Dataset(ncfile, 'r')

lat = dset.variables['lat'][:]
lon = dset.variables['lon'][:]
kedalaman = dset.variables['elevation'][:]

with open(ascii3d, 'w') as tulis_file:
	datawriter = csv.writer(tulis_file, delimiter=',')
	#datawriter.writerow(['bujur', 'lintang', 'kedalaman'])
	for i in xrange(len(lon)):
    #biar tenang nunggunya, lebih baik perlihatkan progress
    print 'progress', i
		for j in xrange(len(lat)):
			datawriter.writerow([lon[i], lat[j], kedalaman[j,i]])
