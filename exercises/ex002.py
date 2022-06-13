# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 22:36:48 2022

@author: bernardogoltz

Concatenate two lists index-wise
"""

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

if len(list1) == len(list2):
    
    list3 = []
    
    for i in range(len(list1)):
        list3.append(list1[i]+list2[i])
        
else: 
    print("The lists don't have the same lenght...")
    pass
