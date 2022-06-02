# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:00:33 2022

@author: bernardogoltz
"""

# Simple plot example. 

import matplotlib.pyplot as plt 
import numpy as np

plt.style.use('_mpl-gallery')

x = np.linspace(0,np.pi*2,50)
y = np.sin(x)
y2 = np.cos(x)

# subplots()

fig, ax = plt.subplots(figsize = (6,3))

ax.set_title("Seno de x")

ax.set_xlabel("Valores para o eixo X")
ax.set_ylabel("Valores para o eixo Y")

ax.plot(x,y,linewidth = 2.5,label = 'Seno')
ax.plot(x,y2,linewidth = 2.5,label = 'Cosseno')
ax.legend(loc = 'upper right')