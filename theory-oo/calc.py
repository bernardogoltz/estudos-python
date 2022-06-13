# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:48:22 2022

@author: bernardogoltz
"""

class Calculadora:
    
    def __init__(self , num1 , num2):
        self.num1 = num1 
        self.num2 = num2
        
    def soma(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2 
    
    def mult(self):
        return self.num1 * self.num2 
    
    def divisao(self):
        return round(self.num1/self.num2,3)
    
numeros = Calculadora(2,3)

print(numeros.soma())
print(numeros.subtracao())
print(numeros.mult())
print(numeros.divisao())