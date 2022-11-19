from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 36})
with open('SVR.log') as f:
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
            case=case.replace("CS", "DB")
        elif counter==8:   
            samples=l[9:]
            if (firstline):
                firstline=False
            flag= not flag
            namelist.append(case+"_"+samples)    
        elif counter==7:   
            rmselist.append(float(l[20:]))                    
        counter=counter+1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(60, 30))
  
ax1.plot(namelist,xlist,linewidth=15,label='X')    
ax1.plot(namelist,ylist,dashes=[2, 2, 10, 2],linewidth=15,label='Y')
ax1.plot(namelist,zlist,'--',dashes=(2, 1),linewidth=15,label='Z')
ax1.set_xticklabels(namelist, rotation=60, ha='right')
ax1.legend()
ax1.grid()
ax1.set_ylabel('Coefficient of Determination',fontsize=36)
ax1.set_xlabel('Case study and samplerates',fontsize=36)

ax2.plot(namelist,rmselist,linewidth=15)    
ax2.set_xticklabels(namelist, rotation=60, ha='right')
ax2.grid()
ax2.set_ylabel('RSME (mm)',fontsize=36)
ax2.set_xlabel('Case study and samplerates',fontsize=36)      
plt.savefig('SVR_samplerate.png', dpi=300)     