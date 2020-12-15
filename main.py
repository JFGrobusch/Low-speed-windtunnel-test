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

class datapoint():
    def __init__(self, angle, dim):
        self.dim = dim #dimension (2d or 3d)
        self.name = angle #AoA (deg)
        self.AoA = float(self.name.replace('b','')) #for eventual plotting; removes non float character
        if 'b' in self.name: self.back = True #stores whether or not data point belongs to hysteresis
        else: self.back = False

import os
import matplotlib.pyplot as plt
for dim in ["2D", "3D"]: #3D and 2D will be plotted seperately
    datapoints = []
    angles = os.listdir(os.path.join('Thermal Data', dim)) #retrieve all angles via directory
    if '.DS_Store' in angles: angles.remove('.DS_Store') #this file is generated as hidden sometimes; this line removes it
    for angle in angles: 
        datapoints.append(datapoint(angle, dim)) #this will take a while; getprecession is run when initialising the data point
    AoA_list = []
    AoA_list_back = [] #initialise lists for plotting
    for datapoint in datapoints:
        if datapoint.back == False: AoA_list.append([datapoint.AoA,getprecession(datapoint)]) #add data points to plotabble list
        if datapoint.back == True: AoA_list_back.append([datapoint.AoA,getprecession(datapoint)]) #sort data points into forward and back for color control
    AoA_list = transpose(AoA_list) #transpose lists to fit matplotlib format
    AoA_list_back = transpose(AoA_list)
    plt.plot(AoA_list)
    plt.plot(AoA_list_back)
    plt.show()
        
