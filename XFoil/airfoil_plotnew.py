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


"""
Get xfoil data
"""
alpha = df.alpha.to_numpy()  # the data is in strings by default
alpha = np.array([float(i) for i in alpha])  # convert

CL = df.CL.to_numpy()  # the data is in strings by default
CL = np.array([float(i) for i in CL])  # convert

CD = df.CD.to_numpy()  # the data is in strings by default
CD = np.array([float(i) for i in CD])  # convert

CM = df.CM.to_numpy()  # the data is in strings by default
CM = np.array([float(i) for i in CM])  # convert

"""
Get test data
"""
import data_analysis_2D as td

#plot
fig, axs = plt.subplots(2, 2)
fig.suptitle("Simulated and tested performance characteristics of the airfoil")
fig.tight_layout(pad=3)
axs[0, 0].plot(alpha, CL, 'tab:red', label = "XFOIL")
axs[0, 0].plot(td.alpha(), td.cl(), 'tab:blue', label = "Delft LSWT")
axs[0, 0].set_title('CL vs. alpha')
axs[0, 1].plot(CD, CL, 'tab:red', label = "XFOIL")
axs[0, 1].plot(td.cd(), td.cl(), 'tab:blue', label = "Delft LSWT")
axs[0, 1].set_title('CL vs. CD')
axs[1, 0].plot(alpha, CM, 'tab:red', label = "XFOIL")
axs[1, 0].plot(td.alpha(), td.cm(), 'tab:blue', label = "Delft LSWT")
axs[1, 0].set_title('CM vs. alpha')
axs[1, 1].plot(alpha, CD, 'tab:red', label = "XFOIL")
axs[1, 1].plot(td.alpha(), td.cd(), 'tab:blue', label = "Delft LSWT")
axs[1, 1].set_title('CD vs. alpha')

axs[0, 0].set(xlabel="Angle of attack [deg]", ylabel="Coefficient of lift [-]")
axs[0, 1].set(xlabel="Coefficient of lift [-]", ylabel="Coefficient of drag [-]")
axs[1, 0].set(xlabel="Angle of attack [deg]", ylabel="Coefficient of moment [-]")
axs[1, 1].set(xlabel="Angle of attack [deg]", ylabel="Coefficient of drag [-]")

#legend
custom_lines = [plt.Line2D([0], [0], color='r', lw=4),
                plt.Line2D([0], [0], color='b', lw=4)]

fig.legend(custom_lines, ['XFOIL', 'Delft LSWT'], loc='center')

fig.show()
