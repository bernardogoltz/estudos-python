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
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("{} -> R$ {}".format(self.saldo , self.titular))
        
    def depositar(self , valor):
        self.saldo += valor
    
    def sacar(self , valor):
        self.saldo -= valor

