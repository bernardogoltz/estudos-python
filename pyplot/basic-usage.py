# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:35:33 2022

@author: bernardogoltz
"""

import matplotlib.pyplot as plt
import numpy as np 

x = [1,2,3,4] # domain
y = np.sqrt(x) # x -> y 

# Matplotlib graphs the data in Figures. 
# Each figure can contain one or more Axes. 

figure, axes = plt.subplots(figsize = (12,6))   

# The function .plot(x,y) will generate a simple plot and wait the arguments of x and y respectively. 

axes.set_title("Título do gráfico")

axes.set_xlabel("Valores para o eixo X")
axes.set_ylabel("Valores para o eixo Y")

axes.plot(x,y) # plot some data on the axes. 





