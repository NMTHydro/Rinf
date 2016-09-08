## Water balance test
import numpy as np

Ksat = 4.0
pD = 6.0
ET = 7.0

Dlim = 15
Dmin = 1

samp = (1,5,8,10,17,24,35)
M = ['M']
P = ['P']
E = ['E']
Ro = ['Ro']
Re = ['Re'] 
dep = ['dep']

for ppt in samp:

    D = pD + ET - ppt
    if D > 15:
        D = 15
    if D < 1:
        D = 1       
    RO = ppt - ET - Ksat - pD
    if RO < 0:
        RO = 0
    rech = ppt - RO - ET - pD
    if rech < 0:
        rech = 0
    if rech > Ksat:
        rech = Ksat
    pD = D
    delM = ppt - ET - D - RO - rech
    
    M.append(str(delM))
    P.append(str(ppt))
    Ro.append(str(RO))
    Re.append(str(rech))
    dep.append(str(D))


P = np.array(P)
Ro = np.array(Ro)
Re = np.array(Re)
dep = np.array(dep)

data =  np.column_stack((P,Ro,Re,dep,M))
print data
    
    
