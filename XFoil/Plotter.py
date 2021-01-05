import matplotlib.pyplot as plt

def textedit(textfile):
    file = open(textfile, 'r') 
    lines = file.readlines()
    lines = lines[2:]
    llines = []
    for line in lines:
        newline = []
        for element in line.split():
            newline.append(float(element))
        llines.append(newline)
    return llines
def alphaCLCD(data):
    alphalst = []
    CDlst = []
    CLlst = []
    CM_rolllst = []
    CM_pitchlst = []
    CM_yawlst = []
    for lijn in data:
        alphalst.append(lijn[1])
        CDlst.append(lijn[4])
        CLlst.append(lijn[3])
        CM_rolllst.append(lijn[10])
        CM_pitchlst.append(lijn[11])
        CM_yawlst.append(lijn[12])
    #print(CM_pitchlst)
    #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    #print(CM_yawlst)
    return alphalst, CLlst, CDlst, CM_rolllst, CM_pitchlst, CM_yawlst
def start():    
    corr = textedit("corr_test.txt")
    uncorr = textedit("unc_test.txt")
    choice = float(input('Clalpha [0] of CLCD [1] of CM_rollalpha [2] of CM_pitchalpha [3] of CM_Yawalpha [4]?'))

    
    if choice == 0:
        plt.plot(alphaCLCD(corr)[0], alphaCLCD(corr)[1], color = 'b', marker = 'D', linewidth = 0.8, markersize = 5)
        plt.ylabel('$C_{L}$ (-)').set_size(16)
        plt.xlabel('α (deg)').set_size(16)
        plt.legend(['Corrected $C_L$ vs α'],prop={'size': 18})
    elif choice == 1:
        plt.plot(alphaCLCD(corr)[2], alphaCLCD(corr)[1], color = 'b', marker = 'D', linewidth = 0.8, markersize = 5)
        plt.ylabel('$C_{L}$ (-)').set_size(16)
        plt.xlabel('$C_D$ (-)').set_size(16)
        plt.legend(['Corrected $C_L$ vs $C_D$'],prop={'size': 18})
    elif choice == 2:
        plt.plot(alphaCLCD(corr)[0], alphaCLCD(corr)[3], color = 'b', marker = 'D', linewidth = 0.8, markersize = 5)
        plt.ylabel('$C_{M_{roll}}$ (-)').set_size(16)
        plt.xlabel('α (deg)').set_size(16)
        plt.legend(['Corrected $C_{M_{roll}}$ vs $α$'],prop={'size': 18})
    elif choice == 3:
        plt.plot(alphaCLCD(corr)[0], alphaCLCD(corr)[4], color = 'b', marker = 'D', linewidth = 0.8, markersize = 5)
        plt.ylabel('$C_{M_{pitch}}$ (-)').set_size(16)
        plt.xlabel('α (deg)').set_size(16)
        plt.legend(['Corrected $C_{M_{pitch}}$ vs $α$'],prop={'size': 18})
    elif choice == 4:
        plt.plot(alphaCLCD(corr)[0], alphaCLCD(corr)[5], color = 'b', marker = 'D', linewidth = 0.8, markersize = 5)
        plt.ylabel('$C_{M_{yaw}}$ (-)').set_size(16)
        plt.xlabel('α (deg)').set_size(16)
        plt.legend(['Corrected $C_{M_{yaw}}$ vs $α$'],prop={'size': 18})
    elif choice == 5:
        plt.plot(alphaCLCD(corr)[0], alphaCLCD(corr)[2], color = 'b', marker = 'D', linewidth = 0.8, markersize = 5)
        plt.ylabel('$C_D$ (-)').set_size(16)
        plt.xlabel('α (deg)').set_size(16)
        plt.legend(['Corrected $C_D$ vs $α$'],prop={'size': 18})
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.show()
            
    return

start()

