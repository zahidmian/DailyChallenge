# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:26:39 2018

@author: zahid mian
"""

import pandas as pd
import datetime
    
# import results
pats = pd.read_csv("../Data/pats_results_2017.csv", encoding='utf-8')
jax = pd.read_csv("../Data/jax_results_2017.csv", encoding='utf-8')

# change datatype of columns
pats[['Week', 'TotYdO', 'TotYdD', 'Opp.1']] = \
    pats[['Week', 'TotYdO', 'TotYdD', 'Opp.1']].apply(pd.to_numeric, errors='coerce')
jax[['Week', 'TotYdO', 'TotYdD', 'Opp.1']] = \
    jax[['Week', 'TotYdO', 'TotYdD', 'Opp.1']].apply(pd.to_numeric, errors='coerce')

# get correlation for each team
corrp = pats['TotYdD'].corr(pats['Opp.1'], method='pearson')
corrj = jax['TotYdD'].corr(jax['Opp.1'], method='pearson')

ax = pats.plot(title='Yards vs Points Given Up by Defense', kind='scatter', x='TotYdD', y='Opp.1', color='DarkBlue', label='Patriots')
jax.plot(kind='scatter', x='TotYdD', y='Opp.1', color='Green', label='Jaguars', ax=ax)
ax.set_xlabel('Yards Given Up by Defense')
ax.set_ylabel('Opponent Score')
ax.text(150, 30, 'correlation\nNWE: %.2f\nJAX: %.2f'%(corrp, corrj), style='italic',
        bbox={'facecolor':'red', 'alpha':0.25, 'pad':5})

now = datetime.datetime.now()
filename = '%d%.02d%.02d.png' % (now.year, now.month, now.day)
plt.savefig(filename, dpi=200)