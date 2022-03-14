# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:48:37 2022
@title: pessoa orientada a objetos. 
@author: bernardogoltz
"""

class Pessoa: 
    # notação d classe em letra maíuscula 
    
    def __init__(self, nome, idade): 
        self.__nome = nome
        self.__idade = idade
        
    # "__init__" função construtora da classe, "__" define um método especial
    # o parâmetro self é uma convenção e refere-se ao próprio objeto. 
    
    
    @property
    def nome(self): 
        print("executando @property nome")
        return self.__nome.title()
    
        # getter -> método get, retorna um atributo de um objeto. 
        # método title trata o nome e devolve em letra maíuscula. 
        
    @nome.setter 
    # notação da propriedade em setters -> atributo.metodo
    def nome(self , nome):
        print("exec. setter")
        self.__nome = nome 

        
