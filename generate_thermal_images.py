#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:10:32 2020

generate grayscale images of all angles of attack, averaged over 9 timestamps

@author: jangrobusch
"""

import numpy as np
from PIL import Image
import os
import sys

def genimage(angle, D):
    #retrieve data
    directory = os.path.join('Thermal Data', D, angle)
    names = []
    for name in os.listdir(directory):
        names.append(os.path.join(directory, name))
    basearray = np.genfromtxt(names[0], delimiter=';') #get base array
    basearray = np.delete(basearray, -1, axis=1)
    basearray = basearray[..., np.newaxis]
    names.remove(names[0])
    p = 0
    print(angle, "deg AoA",round(100*p/9), "% processed")
    for name in names:
        p += 1    
        print(angle, "deg AoA",round(100*p/9), "% processed")
        sample = np.genfromtxt(name, delimiter = ';')
        sample = np.delete(sample, -1, axis=1)
        sample = sample[..., np.newaxis]
        basearray = np.concatenate((basearray, sample), axis=2)
    temparray = np.mean(basearray, axis = 2)    #average data
    #normalise
    mint = np.min(temparray) #Retrieve min and max temps to normalise image
    temparray = temparray - mint
    maxt = np.max(temparray)
    temparray = temparray * (255/maxt)
    im = Image.fromarray(temparray)
    im = im.convert("RGB")
    im.save(os.path.join((D+' thermal images'),(angle+ '.jpg')), "JPEG")
    return()


for dim in ["2D", "3D"]:
    angles = os.listdir(os.path.join('Thermal Data', dim))
    if '.DS_Store' in angles: angles.remove('.DS_Store')
    for angle in angles: genimage(angle, dim)


