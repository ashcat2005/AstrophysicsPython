#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:30:41 2017

@author: ashcat

Calculates the Lorentz Gamma function for the value of normalized velocity 
v/c entered by the user.

"""

import math as m

# Definition of the Lorentz Gamma Function
def gamma (v):
    g = 1/m.sqrt(1-v**2)
    return g

# Value of the velocity to calculate Gamma as beta = v/c ( 0 < beta < 1)
beta = 0.7

#Print the value of the Lorentz Gamma Function
print(gamma(beta))