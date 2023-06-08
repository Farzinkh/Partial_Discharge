import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')
plt.rcParams.update({'font.size':15})
plt.rc('xtick', labelsize=36) 
plt.rc('ytick', labelsize=36) 

#plt.rc('xtick', labelsize=26) 
#plt.rc('ytick', labelsize=26) 
logfile='../../logs/Xgboost/xgboost.log'
save_path='../../logs/Xgboost/samples.png'
with open(logfile) as f:
    lines = f.readlines()   
flag=False
firstline=True
labels_size=36
axis_size=20
counter=1
linenumber=0
xlist,ylist,zlist,rmselist,namelist=[],[],[],[],[]
for l in lines:
    l=l.strip()
    linenumber=linenumber+1
    if l=="---------------------------------":
        flag= not flag
        counter=0
    elif(flag==False or firstline): 
        if counter==1:   
            x=l[27:]
            xlist.append(float(x))
        elif counter==2:   
            ylist.append(float(l[27:]))
        elif counter==3:   
            zlist.append(float(l[27:]))
        elif counter==5:   
            case=l
            case=case.replace("CS","DS")
        elif counter==8:   
            samples=l[9:]
            if (firstline):
                firstline=False
            flag= not flag
            namelist.append(case+"_"+samples)    
        elif counter==7:   
            rmselist.append(float(l[20:]))                    
        counter=counter+1

xlist,ylist,zlist=np.array(xlist),np.array(ylist),np.array(zlist)
r_mean=(xlist+ylist+zlist)/3
barWidth = 0.25

plt.figure(figsize = (17, 9))
# set height of bar

# for i in range(len(namelist)):
#     plt.text(i, x_r[i]/2, str(round(x_r[i],2)), ha = 'center',fontsize = 20)

# for i in range(len(y_r)):
#     plt.text(i+barWidth, y_r[i]/2, str(round(y_r[i],2)), ha = 'center',fontsize = 20)

# for i in range(len(z_r)):
#     plt.text(i+(2*barWidth), z_r[i]/2, str(round(z_r[i],2)), ha = 'center',fontsize = 20)

# Set position of bar on X axis
address={}
sample_rates=['_50','_100','_200','_400','_800','_1200','_2400','_4800']
Sample_rates=[]
for i in sample_rates:
    address[i]=[]
    Sample_rates.append(i[1:])
for ii,i in enumerate(namelist):
    for j in sample_rates:
        if i.find(j)>0:
            address[j].append(ii)
    

br1 = np.arange(len(sample_rates))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]

# Make the plot
L=[]
for k,v in address.items():
    L.append(r_mean[v[0]])
plt.bar(br1, L, width = barWidth,
        label ='DS1')
L=[]
for k,v in address.items():
    L.append(r_mean[v[1]])
plt.bar(br2, L, width = barWidth,
        label ='DS2')
L=[]
for k,v in address.items():
    L.append(r_mean[v[2]])
plt.bar(br3, L, width = barWidth,
        label ='DS3')


# Adding Xticks
plt.xlabel('Number of Samples', fontweight ='bold', fontsize = 30)
plt.ylabel('Correlation Coefficient (R)', fontweight ='bold', fontsize = 30)
plt.xticks([r + barWidth for r in range(len(sample_rates))],
        Sample_rates)
plt.grid()
plt.legend()

plt.savefig(save_path,dpi=500)