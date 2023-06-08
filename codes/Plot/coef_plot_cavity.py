
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')
plt.rcParams.update({'font.size':15})
plt.rc('xtick', labelsize=36) 
plt.rc('ytick', labelsize=36) 

T2_Results = pd.read_csv("../../logs/1D_final_case_study_Three_P2_y/prediction_per_actual.csv")
R_Results = pd.read_csv("../../logs/1D_final_case_study_three_reshape_y/prediction_per_actual.csv")
U_Results = pd.read_csv("../../logs/1D_final_case_study_three_upscale_y/prediction_per_actual.csv")

T2_pred = T2_Results[T2_Results['kind'] == 'predict']
T2_act = T2_Results[T2_Results['kind'] == 'actual']

R_pred = R_Results[R_Results['kind'] == 'predict']
R_act = R_Results[R_Results['kind'] == 'actual']

U_pred = U_Results[U_Results['kind'] == 'predict']
U_act = U_Results[U_Results['kind'] == 'actual']



def calc_r(data_act,data_pred,coordinate):
  return np.corrcoef(data_act[coordinate],data_pred[coordinate])[0][1]

cordinate = 'x'
x_r = [calc_r(T2_pred,T2_pred,cordinate), calc_r(R_act,R_pred,cordinate),calc_r(U_act,U_pred,cordinate) ]
cordinate = 'y'
y_r = [calc_r(T2_act,T2_pred,cordinate), calc_r(R_act,R_pred,cordinate),calc_r(U_act,U_pred,cordinate) ]
cordinate = 'z'
z_r = [calc_r(T2_act,T2_pred,cordinate), calc_r(R_act,R_pred,cordinate),calc_r(U_act,U_pred,cordinate)]

barWidth = 0.25

plt.figure(figsize = (17, 9))
# set height of bar

for i in range(len(x_r)):
    plt.text(i, x_r[i]/2, str(round(x_r[i],2)), ha = 'center',fontsize = 20)

for i in range(len(y_r)):
    plt.text(i+barWidth, y_r[i]/2, str(round(y_r[i],2)), ha = 'center',fontsize = 20)

for i in range(len(z_r)):
    plt.text(i+(2*barWidth), z_r[i]/2, str(round(z_r[i],2)), ha = 'center',fontsize = 20)

# Set position of bar on X axis
br1 = np.arange(len(x_r))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]

# Make the plot
plt.title('Correlation Coefficien (R)',fontweight ='bold', fontsize = 36)
plt.bar(br1, x_r, width = barWidth,
        label ='X')
plt.bar(br2, y_r, width = barWidth,
        label ='Y')
plt.bar(br3, z_r, width = barWidth,
        label ='Z')

# Adding Xticks
plt.xlabel('Models', fontweight ='bold', fontsize = 30)
plt.ylabel('Correlation Coefficient (R)', fontweight ='bold', fontsize = 30)
plt.xticks([r + barWidth for r in range(3)],
        ['Initial shape', 'Reshape', 'Upscale'])
plt.grid()
plt.legend()

plt.savefig('../../logs/Coefficient_Cavity_Shape.png',dpi=500)