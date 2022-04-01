# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:20:21 2022
@author: bernardogoltz
"""

class Employee:
    def __init__(self, first, last, pay):
       
        self.first = first
        self.last = last
        self.pay = pay
        
        self.email = first+'.'+last+'@company.com'
        
    def Describe(self):
        return 'Nome: {} {} - E-Mail: {}'.format(self.first, self.last,self.email)
    
emp_1 = Employee('Tharsilo' , 'Camilo' , 5000)

print(Employee.Describe(emp_1))
# print(emp_1.Describe())
