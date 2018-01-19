# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:20:17 2018

@author: zahid mian
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# import results
nwe = pd.read_csv("../Data/pats_results_2017.csv", encoding='utf-8')
jax = pd.read_csv("../Data/jax_results_2017.csv", encoding='utf-8')
teams = pd.read_csv("../Data/nfl_teams.csv", encoding='utf-8')
teams = teams.rename(index=str, columns={"Team Name":"Opp"})

#nwe = nwe.merge(teams, on=('Opp'), suffixes=('_l', '_r'))
nwe = nwe.merge(teams, on=('Opp'), suffixes=('_l', '_r')) \
    [['Abbr', 'Tm', 'Opp.1', 'TotYdO', 'TotYdD', 'WL']]
jax = jax.merge(teams, on=('Opp'), suffixes=('_l', '_r')) \
    [['Abbr', 'Tm', 'Opp.1', 'TotYdO', 'TotYdD', 'WL']]

#
c = np.intersect1d(
        nwe[nwe['Abbr'].notnull()]['Abbr'], 
        jax[jax['Abbr'].notnull()]['Abbr'])

nwe = nwe[nwe['Abbr'].isin(c)]
jax = jax[jax['Abbr'].isin(c)]

# change datatype of columns
nwe[['TotYdO', 'TotYdD', 'Opp.1']] = \
    nwe[['TotYdO', 'TotYdD', 'Opp.1']].apply(pd.to_numeric, errors='coerce')
jax[['TotYdO', 'TotYdD', 'Opp.1']] = \
    jax[['TotYdO', 'TotYdD', 'Opp.1']].apply(pd.to_numeric, errors='coerce')

#print(c)

nwe_desc = nwe[['Tm', 'Opp.1', 'WL']].groupby(['WL']).describe(percentiles=[]).round()
jax_desc = jax[['Tm', 'Opp.1', 'WL']].groupby(['WL']).describe(percentiles=[]).round()
desc = pd.concat([nwe_desc, jax_desc])

desc.to_html('win_loss_summary.html')


