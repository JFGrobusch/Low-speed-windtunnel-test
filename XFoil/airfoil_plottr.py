from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


"""
todo implement turbulence
todo implement viscosity
    is part of xfoil, use cmd v 
"""

pd.set_option('display.expand_frame_repr', False)
df_raw = pd.read_csv("sim.csv")  # raw output of XFoil from the polar mode

df = pd.read_csv("simtr1.csv", skiprows=10, sep="  ", engine="python")
# skips the data info rows and orders data into columns creating a dataframe df

df = df.drop(0)  # drops the row with dashed lines from XFoil
print(df)
# df.to_csv("sim2.csv", sep=" ", columns=["alpha"])
# now the dataframe has a first row designated with 1 instead of 0


"""
Get xfoil data
"""
alpha = df.alpha.to_numpy()  # the data is in strings by default
alpha = np.array([float(i) for i in alpha])  # convert

Top_Xtr = df.Top_Xtr.to_numpy()  # the data is in strings by default
Top_Xtr = np.array([float(i) for i in Top_Xtr])  # convert

Bop_Xtr = df.Bop_Xtr.to_numpy()  # the data is in strings by default
Bop_Xtr = np.array([float(i) for i in Bop_Xtr])  # convert

"""
Get test data
"""
import data_analysis_2D as td

#plot


