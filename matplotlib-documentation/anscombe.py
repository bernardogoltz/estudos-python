# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:45:05 2022

@author: angel
"""

import seaborn as sns


anscombe = sns.load_dataset('anscombe')
print(anscombe.head(20))

sns.lmplot(data = anscombe , x = "x" , y = "y" , hue = "dataset" , col = "dataset")