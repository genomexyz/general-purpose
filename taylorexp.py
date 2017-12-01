#!/usr/bin/python

#install xlsxwriter dengan sudo -H pip install xlsxwriter

import matplotlib.pyplot as plt
import numpy as np
import pickle
import skill_metrics as sm
from sys import version_info

dataobs = [0, 0, 0, 0, 0, 0, 0, 10, 44, 9, 0, 0, 0, 0, 0, 0, 0, 0]
datamodel = [0, 0, 0, 0, 0, 0, 2.2, 9.5, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
datamodel2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0, 0]

test = sm.taylor_statistics(datamodel,dataobs,'data')
test2 = sm.taylor_statistics(datamodel2,dataobs,'data')

# Store statistics in arrays
sdev = np.array([test['sdev'][0], test['sdev'][1], test2['sdev'][1]])
crmsd = np.array([test['crmsd'][0], test['crmsd'][1], test2['crmsd'][1]])
ccoef = np.array([test['ccoef'][0], test['ccoef'][1], test2['ccoef'][1]])

#print sdev
#print data.ref
sm.taylor_diagram(sdev,crmsd,ccoef)

# Show plot
plt.show()
