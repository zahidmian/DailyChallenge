# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:26:22 2018

@author: zahid mian
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime

with plt.xkcd():

    fig = plt.figure(dpi=100)
    # Add an axes at position rect [left, bottom, width, height] 
    # where all quantities are in fractions of figure width and height.
    #ax = fig.add_axes((0.1, 0.25, 0.8, 0.8))
    ax = fig.add_axes((.2, .2, 1, 1))
    # Make a bar plot with rectangles bounded by (left, right, bottom and top edges)
    # easy just to hardcode these values
    sacks = [242, 381, 286, 352, 4]
    ax.bar(range(0, len(sacks)), sacks, .25)
    # print values above bars
    for i, v in enumerate(sacks):        
        ax.text(i, v, str(v), color='red', fontweight='bold')
    
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4', 'OT' ])
    plt.yticks(range(0, 450, 100))
#
    plt.title("SACKS by Quarter\nNFL 2017")
#
    fig.text(
        0.5, 0.05,
        'Defenses get second wind in 2nd/4th quarters?',
        ha='center')
    
    #plt.show()    
    
    now = datetime.datetime.now()
    filename = '%d%.02d%.02d.png' % (now.year, now.month, now.day)
    plt.savefig(filename, dpi=150)    