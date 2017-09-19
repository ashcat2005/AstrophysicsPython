#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:30:41 2017

@author: ashcat

Calculates the Lorentz Gamma function for a list of values of normalized velocity 
v/c and store these values in the file LorentzGamma.txt

"""

import math as m

# open the file to write the results
outfile = open ("LorentzGamma.txt","w")



# Definition of the Lorentz Gamma Function
def gamma (v):
    g = 1/m.sqrt(1-v**2)
    return g

# Number of steps in the calculation of the Lorentz Gamma Function
steps = 10000

# Write the Header
outfile.write("Beta (v/c)\t Gamma \n")

#Print the value of the Lorentz Gamma Function for values  0 < beta < 1 
# in steps steps
for i in range(steps):
    beta = 0. + i/steps
    g = gamma(beta)
    outstring = "%g" %beta + "\t\t %.6g \n" % g
    outfile.write(outstring)
    
outfile.close()