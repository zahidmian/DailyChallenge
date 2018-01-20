# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:37:57 2018

@author: zahid mian
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

playtypes = pd.read_csv("../Data/nfl_playtype_by_team_2017.csv", encoding='utf-8')
# pivot the data 
playtypes = pd.pivot_table(playtypes, index=['Team'], columns='PlayType')

# create plot
fig, ax = plt.subplots()
fig.set_dpi(200)
groups = len(playtypes)
index = np.arange(groups)
bar_width = 0.4
opacity = 0.8

rects1 = plt.bar(index, playtypes.Freq.PASS, bar_width,
                 alpha=opacity,
                 color='b',
                 label='PASS')
 
rects2 = plt.bar(index + bar_width, playtypes.Freq.RUSH, bar_width,
                 alpha=opacity,
                 color='g',
                 label='RUSH')
 
plt.xlabel('Team')
plt.ylabel('Frequency of Plays')
plt.title('Frequency of Play Type\nNFL 2017')
plt.xticks(index + bar_width, playtypes.index.values)
plt.tick_params(axis='both', which='major', labelsize=4)
plt.legend()
 
plt.tight_layout()
#plt.show()

now = datetime.datetime.now()
filename = '%d%.02d%.02d.png' % (now.year, now.month, now.day)
plt.savefig(filename, dpi=200)