#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:10:32 2020

test environment

@author: jangrobusch
"""

import numpy as np
from PIL import Image

sample = np.genfromtxt('Thermal Data/2D/-1/Record_2020-12-10_12-45-10_0.csv', delimiter=';')
sample = np.delete(sample, -1, axis=1) #last column has all nan values; delete column. #np.delete maybe inefficient for this purpose
maxt = np.max(sample)
mint = np.min(sample) #Retrieve min and max temps to normalise image
sample = sample - mint
sample = sample * (255/maxt)
im = Image.fromarray(sample)
im = im.convert("RGB")
im.save("test", "JPEG")
