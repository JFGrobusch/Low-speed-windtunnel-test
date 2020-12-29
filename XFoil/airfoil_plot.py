from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

"""
todo implement turbulence
todo implement viscosity
    is part of xfoil, use cmd v 
"""

r1 = pd.read_csv("sim.csv")  # raw output of XFoil from the polar mode
r2 = pd.read_csv("sim.csv", skiprows=10)  # skips the plot info rows
# print(r1)
print(r2.iloc[[9]])

