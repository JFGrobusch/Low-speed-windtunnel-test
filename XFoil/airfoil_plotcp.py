from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('display.expand_frame_repr', False)
df_raw = pd.read_csv("simcp.csv")  # raw output of XFoil from the polar mode

df = pd.read_csv("simcp.csv", skiprows=2, sep="  ", engine="python")
# skips the data info rows and orders data into columns creating a dataframe df
f = open("simcp.csv")
print(f for i in f)

df = df.drop(0)  # drops the row with dashed lines from XFoil
# df.to_csv("sim2.csv", sep=" ", columns=["alpha"])
# now the dataframe has a first row designated with 1 instead of 0


"""
Get xfoil data
"""

"""
Get test data
"""
import data_analysis_2D as td

#plot
# plots_x = 2
# plots_y = 2
# fig, axs = plt.subplots(plots_x, plots_y, figsize=(8, 8))
# fig.suptitle("Simulated performance characteristics of the airfoil")
# fig.tight_layout(pad=3)
# axs[0, 0].plot(alpha, CL, 'tab:red', label = "CL")
# axs[0, 0].set_title('CL vs. alpha')
# axs[0, 1].plot(CD, CL, 'tab:green', label = "CL")
# axs[0, 1].set_title('CL vs. CD')
# axs[1, 0].plot(alpha, CM, 'tab:blue', label = "CM")
# axs[1, 0].set_title('CM vs. alpha')
# axs[1, 1].plot(alpha, CD, 'tab:orange', label = "CD")
# axs[1, 1].set_title('CD vs. alpha')
# axs[1, 1].legend()
#
# for x in range(plots_x):
#     for y in range(plots_y):
#         axs[x, y].grid(axis="both")
#         axs[x, y].legend()
#
# axs[0, 0].set(xlabel="Angle of attack [deg]", ylabel="Coefficient of lift [-]")
# axs[0, 1].set(xlabel="Coefficient of drag [-]", ylabel="Coefficient of lift [-]")
# axs[1, 0].set(xlabel="Angle of attack [deg]", ylabel="Coefficient of moment [-]")
# axs[1, 1].set(xlabel="Angle of attack [deg]", ylabel="Coefficient of drag [-]")
#
# fig.show()
# fig.savefig("test")

