# -*- coding: utf-8 -*-
"""
Square every item 

"""

numbers = [1, 2, 3, 4, 5, 6, 7]

def square_a_list(n_list):
    
    solution = []
    
    for item in n_list:
        solution.append(item**2)
    
    return solution

print(square_a_list(numbers))
        
