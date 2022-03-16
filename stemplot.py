# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:07:22 2022

@author: bernardogoltz

"""

#libs
import matplotlib.pyplot as plt
import numpy as np

# making the random data
x = np.arange(0,8)
y = np.random.uniform(1,7 , len(x))

fig , ax = plt.subplots()

ax.stem(x,y)

ax.set(xticks = np.arange(1,8),
       yticks = np.arange(1,8))

plt.show()
