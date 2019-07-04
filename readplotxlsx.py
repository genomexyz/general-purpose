#!/usr/bin/python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap

#setting
excelfile = 'densitas_phase3_kelvin_107.xlsx'
sheetname = 'Sheet1'
resolusi = 1.

dfs = pd.read_excel(excelfile, sheet_name=sheetname)
lat = np.array(dfs['Latitude'])
lon = np.array(dfs['Longitude'])
data = np.array(dfs['Total_Kerapatan'])

#cari tahu dalam 2 dimensi data yang di load berapa x berapa (total grid lat x total grid lon)
data = np.reshape(data, (30, 90))
lat = np.reshape(lat, (30, 90))
lon = np.reshape(lon, (30, 90))

###############
#plotting time#
###############

m = Basemap(resolution='h', projection='merc', \
llcrnrlon=70., llcrnrlat=-15., urcrnrlon=160, urcrnrlat=15) #for mercator

#draw map coastline, etc
m.drawcoastlines(linewidth=0.75)
m.drawcountries(linewidth=0.75)

#make our lon and lat 2D
lon1, lat1 = np.meshgrid(lon[0], lat[:,0])

#for NDVI
plt.title('insert title here')
cs = m.pcolormesh(lon1, lat1, np.squeeze(data), cmap='coolwarm', latlon=True)
cbar = m.colorbar(cs, location='bottom', pad="10%") #add color bar
plt.show()
