#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:10:28 2020

various tools used by other programmes

when entering folder name, do so as a string in the form 'xxx' with no space before the name

@author: jangrobusch
"""
from PIL import Image
import numpy as np
import os

def getarray(angle, dim): #generates numpy array from saved jpeg files (faster than CSV processing)
    directory = os.path.join(dim+' thermal images', angle+'.jpg') #generate file path  
    im = Image.open(directory).convert('L') #read as pillow Image file, convert to grayscale
    array = np.array(im) #convert pillow Image file to numpy array
    return(array)

#folder name must be pre existing
def savearray(array, folder_name, angle, dim): #saves numpy array as jpeg file into specified folder with correct nomenclature
    im = Image.fromarray(array) #generate pillow image from array
    im.convert("RGB")   #specify image type to pillow
    im.save(os.path.join((dim+' '+folder_name),(angle+ '.jpg')), "JPEG") #generate image and save to indicated folder
    return()

def transpose(inlist): #transposes a python list: do not use this with larger lists, very inefficient
    array = np.array(inlist)
    transpose = array.T
    outlist = transpose.tolist()
    return(outlist)

D = "3D"
angle = "0"
savearray(getarray(angle,D), "test", angle, D)