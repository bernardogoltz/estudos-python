# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:56:38 2022

@author: bernardogoltz
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

# making the data for barplot

x = np.arange(8)
    # create a 0 to 8 numpy.ndarray
    
y = np.random.uniform(2,7,len(x))
    #the elements are uniformly distributed between the (a,b,size) , a,b interval. 


# plotting the graphic
fig , ax = plt.subplots()

ax.bar(x , y , width = 1 , edgecolor = "white" , linewidth = 2)

plt.show()


for i in range(len(x)):
    print(type(x[i]))
    # each item of the ndarray created by arange function is an integer