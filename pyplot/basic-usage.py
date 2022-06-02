# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:35:33 2022

@author: bernardogoltz
"""

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,100,5) # domain
y = np.sqrt(x) # x -> y 

# Matplotlib graphs the data in Figures. 
# Each figure can contain one or more Axes. 

figure, axes = plt.subplots(figsize = (10,6))   

# The function .plot(x,y) will generate a simple plot and wait the arguments of x and y respectively. 

axes.set_title("Título do gráfico", fontsize = 30)

axes.set_xlabel("Valores para o eixo X",fontsize = 20)
axes.set_ylabel("Valores para o eixo Y", fontsize = 20)

axes.plot(x,y) # plot some data on the axes. 






