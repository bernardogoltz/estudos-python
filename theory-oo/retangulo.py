# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:47:52 2022

@title: retangulo
@author: bernardogoltz
"""
class Retangulo:
    
    def __init__(self, b, h):
        self.__b = b
        self.__h = h 
        self.__area = b*h

    def area(self):
        return self.__area
    
b = Retangulo(20,50)
print(b._Retangulo__area)