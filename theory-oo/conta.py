# -*- coding: utf-8 -*-

"""
Created on Sat Mar 12 14:14:39 2022

@title: conta.py
@author: bernardogoltz
"""

class Conta: 
    
    # __function__ -> função construtora. 
    
    def __init__(self , numero , titular , saldo , limite):
        print("Construindo objeto: {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("{} -> R$ {}".format(self.__saldo , self.__titular))
        
    def depositar(self , valor):
        self.__saldo += valor
    
    def sacar(self , valor):
        self.__saldo -= valor

