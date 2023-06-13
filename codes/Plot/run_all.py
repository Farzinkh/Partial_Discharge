import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os
import math
import statistics
#import tensorflow_addons as tfa
from tensorflow.keras import layers,Model
from sklearn.model_selection import train_test_split
from tensorflow.keras import backend as K
plt.style.use('seaborn-white')
plt.rcParams.update({'font.size':15})
tf.test.gpu_device_name()


def load_db(label_name,typee):
    if label_name=="THREE_P1" or label_name=="THREE_P2" or label_name=="THREE_RESHAPE" or label_name=="THREE_UPSCALE":
        name=label_name+"_"+typee
    else:
        name=label_name
    Data=pd.read_csv("../datasets/DB_{}_SIGNALS.csv".format(name),index_col=0,header=0,compression='gzip')
    l=Data.columns.values.tolist()
    Data=Data.rename(columns={l[0]:"type"})
    del l[0]
    return Data,l,name

def to_df(Data,sample):
    temp=Data.iloc[:,int(sample)]
    temp=temp.loc[temp.notna()]
    s,t = [],[]
    for idx, ele in enumerate(temp.tolist()): 
        if idx % 2 != 0: 
            t.append(ele) 
        else:
            s.append(ele)        
    df1={'port':s,'time':t}
    df1=pd.DataFrame.from_dict(df1)
    return df1

def addlabels(x,y,text):
    for i in range(len(x)):
        plt.text(i,y[i]/2,str(round(float(text[i]))),ha = 'center',fontweight ='bold',fontsize=20)
        

def grouping(values,errors,classes=8):
    m=round(np.mean(values),2)
    sd=round(statistics.stdev(values),2)
    maximum=round(np.max(values),2)
    minimum=round(np.min(values),2)

    step=(maximum-minimum)/classes
    a,row=0,0
    l,clasifynumbers,clasifyerrors=[],{},{}
    for i in range(classes):
        l.append([a,round(a+step)])
        a=step+a
        clasifynumbers[row]=[]
        clasifyerrors[row]=[]
        row+=1
    for ii,i in enumerate(values):
        row=0
        for j in l:
            if (i>=j[0] and i<=j[1]):
                clasifynumbers[row].append(i)
                clasifyerrors[row].append(errors[ii])
                break
            row+=1
    mean,error_mean=[],[]
    for i in range(classes):
        mean.append(round(np.max(clasifynumbers[i])))
        error_mean.append(round(np.mean(clasifyerrors[i])))
    return mean,error_mean

def addlabels2(x,y,text):
    for i in range(len(x)):
        plt.text(i,y[i],str(round(float(text[i]),1))+'%',ha = 'center',fontweight ='bold',fontsize=20)
            
def grouping2(values,classes=8):
    m=np.mean(values)
    sd=statistics.stdev(values)
    maximum=np.max(values)
    minimum=np.min(values)

    step=round((maximum-minimum)/classes,2)
    a,row=0,0
    l,clasifynumbers=[],{}
    for i in range(classes):
        l.append([a,a+step])
        a=step+a
        clasifynumbers[row]=[]
        row+=1
    for i in values:
        row=0
        for j in l:
            if (i>=j[0] and i<=j[1]):
                clasifynumbers[row].append(i)
                break
            row+=1
    variety=[]
    for i in range(classes):
        l[i]=str(round(l[i][0]+step))
        variety.append((len(clasifynumbers[i])/len(values))*100) 

    return l,variety

filter=['1D_final_case_study_Three_P1_y_triple','1D_final_case_study_Three_P2_y_triple','Xgboost','SVR','linear_Regression','Coefficient_Cavity_Shape.png','Models_Coefficient.png','target_vs_estimate_location.png']
folders=os.listdir('../logs')
case_study=[]
for i in folders:
    if i in filter:
        continue
    else:
        index=4
        dataset=i.split('_')[index]
        if dataset=='snn':
            model='snn'
            index+=1
            dataset=i.split('_')[index]
        else:
            model='cnn'
        if dataset=='three' or dataset=='Three':
            index+=1
            origin=i.split('_')[index]
            direction=i.split('_')[index+1]
            if origin=='p1' or origin=='P1':
                dataset="THREE_P1"
            elif origin=='p2' or origin=='P2':
                dataset="THREE_P2"
            elif origin=='reshape':
                dataset="THREE_RESHAPE"
            elif origin=='upscale':
                dataset="THREE_UPSCALE"
            case_study.append([model,dataset,i])
        else:
            if dataset=='one':
                dataset='ONE'
            elif dataset=='two':
                dataset='TWO'
            case_study.append([model,dataset,i])

for case in case_study:
    samplerate=400
    label_name=case[1]
    model_name_to_load=case[2]
    model_name_to_load="../logs/"+model_name_to_load
    model_name_to_save=model_name_to_load                #model_name_to_load
    model=tf.keras.models.load_model('{}/best_model.h5'.format(model_name_to_load))

    testdataframe=pd.read_csv ("{}/test_{}.csv".format(model_name_to_load,samplerate)) 
    traindataframe=pd.read_csv ("{}/train_{}.csv".format(model_name_to_load,samplerate)) 
    y_test = pd.DataFrame({'x':testdataframe['x'],
                'y': testdataframe['y'],
                'z': testdataframe['z']})
    X_test=testdataframe.drop(['x', 'y','z'], axis=1)
    y_train = pd.DataFrame({'x':traindataframe['x'],
                'y': traindataframe['y'],
                'z': traindataframe['z']})
    X_train=traindataframe.drop(['x', 'y','z'], axis=1)

    c,c2,index=0,0,0
    errors={}
    validation={}
    poly_space=[]

    if label_name=="THREE_UPSCALE":
        Xconstant=1000
        Zconstant=500
    else:    
        Xconstant=500
        Zconstant=250
        
    if label_name=="THREE_RESHAPE" or label_name=="THREE_UPSCALE": 
        Yconstant=500
    else:    
        Yconstant=250   
        
        
    for i in model.predict(X_test):
        x,y,z=i
        x2,y2,z2=y_test.to_numpy()[c2]
        validation[c]=[x,y,z,index,'predict']
        c+=1
        validation[c]=[x2,y2,z2,index,'actual']
        poly_space.append(math.sqrt((x2-Xconstant)**2+(y2-Yconstant)**2+(z2-Zconstant)**2))
        c+=1
        c2+=1
        index+=1
        errors[c]=math.sqrt((1/3)*((x2-x)**2+(y2-y)**2+(z2-z)**2))

    validation=pd.DataFrame.from_dict(validation, orient='index',columns=['x','y','z','index','kind'])
    validation.to_csv("{}/prediction_per_actual.csv".format(model_name_to_save),index=False)

    plt.rc('xtick', labelsize=36) 
    plt.rc('ytick', labelsize=36) 
    plt.figure(1,figsize=(17,9))

    groups={}
    groups['POLY_MEAN'],groups['RMSE_MEAN']=grouping(poly_space,list(errors.values()),classes=3)
    print(groups['RMSE_MEAN'],groups['POLY_MEAN'])


    labels=['Corner','Middle','Centre']

    plt.title("Data distribution in cavity",fontweight ='bold',fontsize=36)
    for i in range(len(groups['RMSE_MEAN'])):
        plt.bar(labels[i]+' '+str(groups['POLY_MEAN'][i])+'(mm)',groups['RMSE_MEAN'][i],label=labels[i],edgecolor='black')
    addlabels(labels,groups['RMSE_MEAN'],groups['RMSE_MEAN'])
    plt.ylabel("Average RMSE(mm)",fontweight ='bold',fontsize=30)
    plt.xlabel("Location",fontweight ='bold',fontsize=30)

    plt.grid()

    plt.savefig('{}/Euclidean_distance.png'.format(model_name_to_save),dpi=300)
    plt.cla()
    plt.clf()
    #--------------------------------------------------------------------------------------------------------
    plt.rc('xtick', labelsize=25) 
    plt.rc('ytick', labelsize=25) 
    plt.figure(1,figsize=(17,9))

    values=list(errors.values())
    m=round(np.mean(values),2)
    sd=round(statistics.stdev(values),2)
    maximum=round(np.max(values),2)
    minimum=round(np.min(values),2)
    plt.title("RMSE Mean :{} Standard deviation :{} Max :{} Min :{}".format(m,sd,maximum,minimum),fontweight ='bold',fontsize=28)
    #plt.hist(values, density=True)
    groups['RMSE'],groups['variety']=grouping2(list(errors.values()),classes=8)
    Groups=[]
    for i in range(len(groups['RMSE'])):
        if i==0:
            Groups.append('('+str(0)+'-'+groups['RMSE'][i]+')')
        else:
            Groups.append('('+groups['RMSE'][i-1]+'-'+groups['RMSE'][i]+')')
    plt.bar(Groups,groups['variety'],label='Density')
    t=groups['variety'].copy()
    for i,v in enumerate(groups['variety']):
        v=round(v,2)
        if i==0:
            t[i]=v
        else:
            t[i]=v+t[i-1]

    addlabels2(Groups,groups['variety'],groups['variety'])
    plt.bar(Groups,np.array(t)-np.array(groups['variety']),bottom=groups['variety'],label='Overall density')
    addlabels2(Groups,t,t)
    plt.grid()
    plt.legend(prop = { "size": 30 })
    plt.ylabel("Predict density in percent",fontweight ='bold',fontsize=36)
    plt.xlabel("RMSE(mm)",fontweight ='bold',fontsize=36)

    plt.savefig('{}/losses.png'.format(model_name_to_save),dpi=500)
    plt.cla()
    plt.clf()