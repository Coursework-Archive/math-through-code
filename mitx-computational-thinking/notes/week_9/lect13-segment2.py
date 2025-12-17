# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:19:46 2016

@author: guttag
"""

import random
import matplotlib.pyplot as plt

# set line width
plt.rcParams['lines.linewidth'] = 4
# set font size for titles
plt.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
plt.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
# set size of markers
plt.rcParams['lines.markersize'] = 10
# set number of examples shown in legends
plt.rcParams['legend.numpoints'] = 1

random.seed(0)
numCasesPerYear = 36000
numYears = 3
stateSize = 10000
communitySize = 10
numCommunities = stateSize // communitySize
numTrials = 100
numGreater = 0

for t in range(numTrials):
    locs = [0] * numCommunities
    for i in range(numYears * numCasesPerYear):
        # slightly more efficient than random.choice(range(numCommunities))
        locs[random.randrange(numCommunities)] += 1
    if max(locs) >= 143:
        numGreater += 1

prob = round(numGreater / numTrials, 4)
print('Est. probability of at least one region having '
      'at least 143 cases =', prob)

print('Average number of cases per community =',
      (numYears * numCasesPerYear) / numCommunities)
print('Maximum number of cases in community X =',
      max(locs))

plt.hist(locs)
plt.xlabel('Number of New Cancer Cases')
plt.ylabel('Count of Regions')
plt.title('Distribution of Cancer Cases Across Regions')
plt.show()
