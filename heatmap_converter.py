#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 23:33:41 2020

@author: jangrobusch
"""


#needs work

#https://stackoverflow.com/questions/59478962/how-to-convert-a-grayscale-image-to-heatmap-image-with-python-opencv

import cv2

image = cv2.imread('frame.png', 0)
heatmap = cv2.applyColorMap(image, cv2.COLORMAP_HOT)

cv2.imshow('heatmap', heatmap)
cv2.waitKey()