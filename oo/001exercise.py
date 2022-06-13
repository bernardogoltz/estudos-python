# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 20:04:49 2022

@author: bernardogoltz

"""
import pandas as pd
import glob

class Reader:
    
    def __init__(self,path,columns_name):
        self.path = path 
        self.idx = columns_name
        
    def files_list(self):
        self.files_list = glob.glob(self.path+'/*.dat')
    
    def generate_df(self):
        
        dfListona = []
        
        for item in self.files:
            df_dia = pd.read_csv(item,on_bad_lines = 'warn')
            dfListona.append(df_dia)
        
        df_mes = pd.DataFrame()
        
        for item in dfListona:
            df_mes = pd.concat([df_mes,item])
        
        df_mes = df_mes.set_index(df_mes['Timestamp'])
        df_mes = df_mes.drop(columns = df_mes.columns[0])
        
        return df_mes