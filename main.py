#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:12:15 2020

retrieve streamline procession

test images saved in test directory

modification pending

@author: jangrobusch
"""

from tools import getarray, savearray
import numpy as np

class datapoint():
    def __init__(self, angle, dim):
        self.dim = dim #dimension (2d or 3d)
        self.name = angle #AoA (deg)
        self.AoA = float(self.name.replace('b','')) #for eventual plotting; removes non float character
        if 'b' in self.name: self.back = True #stores whether or not data point belongs to hysteresis
        else: self.back = False
        self.precession = None #initially empty; eventually procession value (%) will be stored here

def getprecession(datapoint):
    def avgdiff(row, reach): #considers [reach] entries preceding and following points in the row to find average of entries
        index = 0
        diffrow = np.zeros_like(row) #gen empty array to write to
        for entry in row:
            low = index-reach
            if low < 0: low = 0 #prevent index error (negartive values not valid)
            high = index+reach+1
            preceding_points = row[low:index]
            following_points = row[index+1:high] #get points before and after point
            avg_pre = np.mean(preceding_points)
            avg_follow = np.mean(following_points) #get averages
            if avg_pre.size < 10 or avg_follow.size < 10: np.put(diffrow, index, 0) #check that array is suitably large (avoid noise)
            else: np.put(diffrow, index, abs(avg_pre-avg_follow))    #returns diffrow              
            index += 1       
        return(diffrow)
    array = getarray(datapoint.name, datapoint.dim) #initialise array
    crop = 80 #number of pixels removed from top and bottom of image (crop). number hard coded
    array = array[crop:array.shape[0]-crop] #crops array to desired dimension
    diffarray = array #copies initial array to new array for modification
    index = 0
    for row in diffarray:
        np.put(diffarray, index, avgdiff(row, 30)) #gets diffrow, writes to np row. using reach (0.5range) of 30 px
        index += 1
    #TROUBLESHOOT; DATA IS NOT CHANGING
    savearray(diffarray, 'test', datapoint.name, datapoint.dim)    
            
    return()

p1 = datapoint("5", "3D")

getprecession(p1)