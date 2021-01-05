#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:12:15 2020

retrieve streamline precession points, overlay on thermal image

@author: jangrobusch
"""

from tools import getarray, savearray, transpose
import numpy as np
from statistics import mean
import sys



def getprecession(angle, dim):    
    print("Generating difference array for", angle, "deg AoA", dim, "case")
    array = getarray(angle, dim) #initialise array
    crop = 70 #number of pixels removed from top and bottom of image (crop). number hard coded
    maxind, y = np.shape(array)
    # array = array[crop:array.shape[0]-crop] #crops array to desired dimension
    
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
            if preceding_points.size < reach or following_points.size < reach: np.put(diffrow, index, 0) #check that array is suitably large (avoid noise)
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
  
        return(likely_transition)

    shape = np.shape(diffarray)
    RGB_transition = np.zeros((*shape, 4)).astype(np.uint8) #generates new RGB array
    
    indexx = 0
    for row in diffarray:
        indexy = processrow(row) #get transition index, trailing edge index, leading edge index
        RGB_transition[indexx, indexy] = (255, 0, 0, 255)
        indexx += 1
    RGB_transition[:crop] = (0, 0 , 0, 0)    
    RGB_transition[-crop:] = (0, 0, 0 , 0)
    return(RGB_transition)




import os
from PIL import Image
datapoints = []
for dim in ["2D", "3D"]: #generate data for 3D and 2D
    angles = os.listdir(os.path.join('Thermal Data', dim)) #retrieve all angles via directory
    if '.DS_Store' in angles: angles.remove('.DS_Store') #this file is generated sometimes; this line removes it
    for angle in angles:
        folder_name = ('transition images')
        im_trans = Image.fromarray(getprecession(angle, dim), ) #image of precession
        directory = os.path.join(dim+' thermal images', angle+'.jpg') #to base
        im_bot = Image.open(directory).convert("RGBA") #thermal image
        im_bot.paste(im_trans, (0,0), im_trans) #paste precession on top
        im_bot.save(os.path.join((dim+' '+folder_name),(angle+ '.png')), "PNG")
        print("working")
    

    

    
        
