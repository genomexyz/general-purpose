#!/usr/bin/python

from mpl_toolkits.basemap import Basemap
from matplotlib import colors
from scipy import misc
import glob
import numpy as np
import csv
import matplotlib.pyplot as plt
import time
import random

#setting
iterasi = 50
initcond1 = 0.5
initcond2 = 0.5001
totinit = 100
resol = 0.01
stdval = 25.0
rangeval = 5.0
rangeprob = 1.0
mintemp = 20.0
totprob = 10



def chaoscal(inp):
	return inp**2.0 - 2

def convtot(val):
	print stdval
	return stdval + val / 2.0 * rangeval

initval = np.zeros((totinit, iterasi))

for i in xrange(totinit):
	initval[i,0] = (0 - totinit/2.0 * resol) + i * resol

#chaotic calculation
for i in xrange(iterasi-1):
	initval[:,i+1] = chaoscal(initval[:,i])


#temperature range
probvec = range(int(mintemp), int(mintemp+rangeprob*totprob+1))

#vector of frequencies
freq = np.zeros((totprob))

for i in xrange(totprob):
	for j in xrange(totinit):
		print probvec[i]
		print convtot(initval[j,-1])
		print probvec[i+1]
		if probvec[i] < convtot(initval[j,-1]) < probvec[i+1]:
			freq[i] += 1
		print

print freq

#plot
for i in xrange(totinit):
	#plt.plot(val1, label='init1')
	plt.plot(initval[i])
	#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)

plt.show()
