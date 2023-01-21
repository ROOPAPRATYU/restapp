import time as tm
t=tm.ctime()
print(t)
tm=t[4]+t[5]+t[6]
td=t[8]+t[9]
ty=t[20]+t[21]+t[22]+t[23]
d={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sept':'09','Oct':'10','Nov':'11','Dec':'12'}
dmm=list(d.keys())
dmn=list(d.values())
for i in range(len(dmm)):
    if dmm[i]==tm:
        tm=(dmn[i])

dmy=str(ty+'-'+tm+'-'+td)
print(dmy)
