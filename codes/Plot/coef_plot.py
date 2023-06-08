
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')
plt.rcParams.update({'font.size':15})
plt.rc('xtick', labelsize=36) 
plt.rc('ytick', labelsize=36) 

LR_Results = pd.read_csv("../../logs/linear_Regression/prediction_per_actual.csv")
XG_Results = pd.read_csv("../../logs/Xgboost/prediction_per_actual.csv")
SVR_Results = pd.read_csv("../../logs/SVR/prediction_per_actual.csv")
CNN_Results = pd.read_csv("../../logs/1D_final_case_study_Three_P2_y/prediction_per_actual.csv")
NN_Results = pd.read_csv("../../logs/1D_final_case_study_snn_three_p2_y/prediction_per_actual.csv")

LR_pred = LR_Results[LR_Results['kind'] == 'predict']
LR_act = LR_Results[LR_Results['kind'] == 'actual']

XG_pred = XG_Results[XG_Results['kind'] == 'predict']
XG_act = XG_Results[XG_Results['kind'] == 'actual']

SVR_pred = SVR_Results[SVR_Results['kind'] == 'predict']
SVR_act = SVR_Results[SVR_Results['kind'] == 'actual']

CNN_pred = CNN_Results[CNN_Results['kind'] == 'predict']
CNN_act = CNN_Results[CNN_Results['kind'] == 'actual']

NN_pred = NN_Results[NN_Results['kind'] == 'predict']
NN_act = NN_Results[NN_Results['kind'] == 'actual']


def calc_r(data_act,data_pred,coordinate):
  return np.corrcoef(data_act[coordinate],data_pred[coordinate])[0][1]

cordinate = 'x'
x_r = [calc_r(SVR_act,SVR_pred,cordinate), calc_r(XG_act,XG_pred,cordinate),calc_r(NN_act,NN_pred,cordinate),calc_r(CNN_act,CNN_pred,cordinate) ]
cordinate = 'y'
y_r = [calc_r(SVR_act,SVR_pred,cordinate), calc_r(XG_act,XG_pred,cordinate),calc_r(NN_act,NN_pred,cordinate),calc_r(CNN_act,CNN_pred,cordinate) ]
cordinate = 'z'
z_r = [calc_r(SVR_act,SVR_pred,cordinate), calc_r(XG_act,XG_pred,cordinate),calc_r(NN_act,NN_pred,cordinate),calc_r(CNN_act,CNN_pred,cordinate) ]

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
plt.xticks([r + barWidth for r in range(4)],
        ['SVR', 'XGBoost', 'BPNN', 'CNN', ])
plt.grid()
plt.legend()

plt.savefig('../../logs/Models_Coefficient.png',dpi=500)