#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:30:41 2017

@author: ashcat

Calculates the Lorentz Gamma function for a list of values of normalized velocity 
v/c and store these values in the file LorentzGamma.txt

"""

import matplotlib.pyplot as pl
import numpy as np


# Definition of the Lorentz Gamma Function (note that we implement the function 
# using the np.sqrt and not the m.sqrt because we need to calculate the values 
# of this function for the values stored in the matrix t1 defined below)
def gamma (v):
    g = 1/np.sqrt(1-v**2)
    return g

# Number of steps in the calculation of the Lorentz Gamma Function
steps = 10000



t1 = np.arange(0.0, 1.0, 1/steps)

pl.plot(t1 , gamma(t1))


# open the file to read the data
infile = open ("LorentzGamma.txt","r")
# read the data
gammaData = infile.readlines()
# close the file again
infile.close()

# get number of data lines in the file 
# (-1, because first line is a comment) 
n = len(gammaData)-1

# allocate two numpy arrays 
time = np.zeros(n)
data = np.zeros(n)

# parse the data 
for i in range(n):
    # use the  split function
    # to split each line into two strings (separated by two tabs)
    splitline = gammaData[i+1][:-1].split('\t\t')
    time[i] = float(splitline[0])
    data[i] = float(splitline[1])   
    
    
# Plot data as ro (red o)  b^ (blue triangles) gs(green squares) etc
pl.plot(time , data, 'r^')

# Plot Labels
pl.xlabel('v/c')
pl.ylabel('gamma')