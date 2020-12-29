#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:12:15 2020

retrieve streamline procession

test images saved in test directory

modification pending

@author: jangrobusch
"""

from tools import getarray, savearray, transpose
import numpy as np
from statistics import mean
import sys



def getprecession(datapoint):
    
    print("Generating difference array for", datapoint.name, "deg AoA", datapoint.dim, "case")
    array = getarray(datapoint.name, datapoint.dim) #initialise array
    crop = 80 #number of pixels removed from top and bottom of image (crop). number hard coded
    array = array[crop:array.shape[0]-crop] #crops array to desired dimension
    
    reach = 10 #reach concerns the number of pixels considered in positive and negative direction
    diffarray = np.zeros_like(array) #copies initial array to new array for modification
    
    #generates new array composed of the difference between the average of 30 preceding and following entries
    
    def avgdiff(row): #considers [reach] entries preceding and following points in the row to find average of entries
        #diffrow array has max value 255 min value 0 and all int; low level of fineness recorded. consider converting array to floats, this will slow down calcs
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
            if preceding_points.size < 10 or following_points.size < 10: np.put(diffrow, index, 0) #check that array is suitably large (avoid noise)
            else: np.put(diffrow, index, abs(avg_pre-avg_follow))    #returns diffrow; only int are recorded, floats are unnecessarily slow           
            index += 1
        return(diffrow)
    index = 0
    for row in array:
        diffarray[index] = avgdiff(row)#gets diffrow, writes to np row
        index += 1 
            
    #refine edges; narrow down to one leading edge, one trailing edge, and transition.
                
    def processrow(row): #gets max value within row; sets all non-max values within reach to 0. Similar procedure 2 more times
        foil_edge_1 = np.argmax(row) #get index of max
        row[foil_edge_1-reach: foil_edge_1+reach+1]=0 #sets midpoint values+range to 0          #index error might occur, fix if necessary
        foil_edge_2 = np.argmax(row) #get index of 2nd max
        row[foil_edge_2-reach: foil_edge_2+reach+1]=0 #sets midpoint values+range to 0 for 2nd edge
        
        likely_transition = np.argmax(row) #likely transition point is remaining maximum
        
        trailing_edge = min(foil_edge_1, foil_edge_2) #gets trailing edge
        leading_edge = max(foil_edge_1, foil_edge_2) #gets leading edge
        chord = leading_edge-trailing_edge #chord length in px
        prc = abs(likely_transition-trailing_edge) #distance from transition to trailing edge in px
        
        transition_pc = prc/chord*100 #percentage procession of chord
        return(transition_pc)
        
    transition_points = [] #empty list to store transition points
    for row in diffarray:
        transition_points.append(processrow(row)) #get transition % from above function
    precession = 100-mean(transition_points) #average transition %, save to object
    print(datapoint.name, datapoint.dim," has turbulent transition at", round(precession) , "% chord from LE")           
    return(precession)

class init(): #datapoint class, stores relevant data
    def __init__(self, angle, dim):
        self.dim = dim #dimension (2d or 3d)
        self.name = angle #AoA (deg)
        self.AoA = float(self.name.replace('b','')) #for eventual plotting; removes non float character
        if 'b' in self.name: self.back = True #stores whether or not data point belongs to hysteresis
        else: self.back = False
        self.precession = None

import os
datapoints = []
for dim in ["2D", "3D"]: #generate data for 3D and 2D
    angles = os.listdir(os.path.join('Thermal Data', dim)) #retrieve all angles via directory
    if '.DS_Store' in angles: angles.remove('.DS_Store') #this file is generated as hidden sometimes; this line removes it
    for angle in angles:
        datapoint = init(angle, dim)
        datapoints.append(datapoint)
    for datapoint in datapoints:
        datapoint.precession = getprecession(datapoint) #calculates precession

datalist = [['Dim', 'AoA', 'Precession %', 'Back']] #extracting data for processing (more stable)      
for datapoint in datapoints:
    data = datapoint.dim, datapoint.AoA, datapoint.precession, datapoint.back
    datalist.append(data) #code self explanatory

# import xlsxwriter library: install this package if not already installed
import xlsxwriter 
  
# initialise file
file = xlsxwriter.Workbook('data.xlsx') 
sheet = file.add_worksheet()

#set row index to 0
row = 0
col = 0
print("Writing to XLSX file")
for dim, aoa, precession, back in (datalist):
    sheet.write(row, col, dim)
    sheet.write(row, col+1, aoa)
    sheet.write(row, col+2, precession)    
    sheet.write(row, col+3, back)
    row += 1

file.close()    
    
    

    
        
