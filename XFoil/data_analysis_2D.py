import matplotlib.pyplot as plt
import matplotlib.lines as mlines


file = "corr_test.txt"

def alpha():
    f = open(file, "r")
    lines = f.readlines()
    alphastr = []
    for line in lines:
        alphastr.append((line.split()[1]))
    alphastr = alphastr[2:]
    alpha = []
    for i in range(len(alphastr)):
        x = float(alphastr[i])
        alpha.append(x)

    return alpha

def cl():
    f = open(file, "r")
    lines = f.readlines()
    clstr = []
    for line in lines:
        clstr.append((line.split()[3]))
    clstr = clstr[2:]
    cl = []
    for i in range(len(clstr)):
        x = float(clstr[i])
        cl.append(x)

    return cl

def cd():
    f = open(file, "r")
    lines = f.readlines()
    cdstr = []
    for line in lines:
        cdstr.append((line.split()[2]))
    cdstr = cdstr[2:]
    cd = []
    for i in range(len(cdstr)):
        x = float(cdstr[i])
        cd.append(x)

    return cd

def cm():
    f = open(file, "r")
    lines = f.readlines()
    cmstr = []
    for line in lines:
        cmstr.append((line.split()[4]))
    cmstr = cmstr[2:]
    cm = []
    for i in range(len(cmstr)):
        x = float(cmstr[i])
        cm.append(x)

    return cm

# legend1 = mlines.Line2D([],[], color = 'blue', label = '$C_{l}$ vs $C_{d}$')
# legend2 = mlines.Line2D([],[], color = 'blue', label = '$C_{l}$ vs α')
# legend3 = mlines.Line2D([],[], color = 'blue', label = '$C_{d}$ vs α')
# legend4 = mlines.Line2D([],[], color = 'blue', label = '$C_{m}$ vs α')


# plt.plot(cd(),cl(), 'b', marker = '.')
# plt.title("Drag polar")
# plt.xlabel("Drag coefficient (-)")
# plt.ylabel("Lift coefficient (-)")
# plt.legend(handles=[legend1], shadow=True, loc=(0.6, 0.15), handlelength=1.5, fontsize=10)
# plt.grid(True)
# plt.show()

# plt.plot(alpha(),cl(), 'b', marker = '.')
# plt.title("Lift coefficient versus angle of attack")
# plt.xlabel("Angle of attack (deg)")
# plt.ylabel("Lift coefficient (-)")
# plt.legend(handles=[legend2], shadow=True, loc=(0.6, 0.15), handlelength=1.5, fontsize=10)
# plt.grid(True)
# plt.show()

# plt.plot(alpha(),cd(), 'b', marker = '.')
# plt.title("Drag coefficient versus angle of attack")
# plt.xlabel("Angle of attack (deg)")
# plt.ylabel("Drag coefficient (-)")
# plt.legend(handles=[legend3], shadow=True, loc=(0.2, 0.3), handlelength=1.5, fontsize=10)
# plt.grid(True)
# plt.show()

# plt.plot(alpha(), cm(), 'b', marker = '.')
# plt.title("Moment coefficient versus angle of attack")
# plt.xlabel("Angle of attack (deg)")
# plt.ylabel("Moment coefficient (-)")
# plt.legend(handles=[legend4], shadow=True, loc=(0.2, 0.1), handlelength=1.5, fontsize=10)
# plt.grid(True)
# plt.show()













