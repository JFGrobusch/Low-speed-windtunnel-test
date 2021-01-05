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

df = pd.read_csv("sim.csv", skiprows=10, sep="  ", engine="python")
# skips the data info rows and orders data into columns creating a dataframe df

df = df.drop(0)  # drops the row with dashed lines from XFoil
# df.to_csv("sim2.csv", sep=" ", columns=["alpha"])
# now the dataframe has a first row designated with 1 instead of 0

lst_alpha = df.alpha.to_numpy()  # the data is in strings by default
lst_alpha = np.array([float(i) for i in lst_alpha])  # convert

lst_CL = df.CL.to_numpy()  # the data is in strings by default
lst_CL = np.array([float(i) for i in lst_CL])  # convert

lst_CD = df.CD.to_numpy()  # the data is in strings by default
lst_CD = np.array([float(i) for i in lst_CD])  # convert

plt.plot(lst_alpha, lst_CL)
plt.title("Alpha vs. CL")
plt.legend("CL")
plt.xlabel("Angle of attack [deg]")
plt.ylabel("Coefficient of lift [-]")
plt.show()

# df.plot(x="CD", y="CL", kind="scatter")
# plt.show()
