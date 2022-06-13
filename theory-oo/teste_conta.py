# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:16:51 2022

@name:python orientado a objetos
@author: bernardogoltz
"""

def criar_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, 
           "titular":titular, 
           "saldo":saldo, 
           "limite":limite}

def deposita(conta , valor):
    conta["saldo"] += valor
    
def saca(conta , valor):
    conta["saldo"] -= valor
    
def extrato(conta):
    print("O saldo é {} ".format(conta["saldo"]))
    




    