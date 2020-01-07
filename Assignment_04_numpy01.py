#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:34:05 2019

@author: karan
"""
# Numpy Assignment to show the column stack functionality of numpy with powerseries
import numpy as np
order = input("In Which order you want the power series : decreasing or increasing\n")
N = 5
def powerseries(N,order):
    vector = np.array([1,2,3,4])
    if order == "decreasing":
        mat = np.column_stack([vector**(N-1-i) for i in range(N)])
        print(mat)
    else:
        mat = np.column_stack([vector**i for i in range(N)])
        print(mat)
powerseries(N,order)

        
