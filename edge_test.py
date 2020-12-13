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

class datapoint():
    def __init__(self, angle):
        self.name = angle
        self.AoA = float(self.name.replace('b','')) #for eventual plotting; removes non float character
        if 'b' in self.name: self.back = True #stores whether or not data point belongs to hysteresis
        else: self.back = False
        self.precession = None #initially empty; eventually procession value (%) will be stored here

test = "1.5"
test = float(test.replace('b',''))
print(2*test)
