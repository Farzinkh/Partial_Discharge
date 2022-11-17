from matplotlib import pyplot as plt
with open('xgboost.log') as f:
    lines = f.readlines()   
flag=False
firstline=True
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
        elif counter==8:   
            samples=l[9:]
            if (firstline):
                firstline=False
            flag= not flag
            namelist.append(case+"_"+samples)    
        elif counter==7:   
            rmselist.append(float(l[20:]))                    
        counter=counter+1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
  
ax1.plot(namelist,xlist,label='X')    
ax1.plot(namelist,ylist,label='Y')
ax1.plot(namelist,zlist,label='Z')
ax1.set_xticklabels(namelist, rotation=60, ha='right')
ax1.legend()
ax1.grid()
ax1.set_ylabel('R2')
ax1.set_xlabel('Case study and samplerates')

ax2.plot(namelist,rmselist)    
ax2.set_xticklabels(namelist, rotation=60, ha='right')
ax2.grid()
ax2.set_ylabel('RSME')
ax2.set_xlabel('Case study and samplerates')
plt.show()           