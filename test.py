#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 12:28:06 2020

@author: jangrobusch
"""

import numpy as np

a = np.zeros((4, 4))

a[-1:] = 1
a[:1] = 1
print(a)


