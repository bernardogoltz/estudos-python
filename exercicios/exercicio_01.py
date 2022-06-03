# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:17:20 2022

@author: bernardogoltz

Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

"""

class Vehicle():
    
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
    def infos(self):
        print("max speed: {}\nmileage: {}\n".format(self.max_speed,self.mileage))
        

model_s =  Vehicle(200,10000)
model_s.infos()

# =============================================================================
# max speed: 200
# mileage: 10000
# =============================================================================
