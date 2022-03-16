# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:16:08 2022

@author: angel
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,8,24)

y1 = 2*x/3 + np.random.uniform(0.0, 0.5, len(x))
y2 = 3*x/9 + np.random.uniform(0.0, 0.5, len(x)) 


# plot = 
fig , ax = plt.subplots()

ax.fill_between(x , y2, y1 , alpha = 0.50 , linewidth = 0)
ax.plot(x , (y1+y2)/2, linewidth = 2)