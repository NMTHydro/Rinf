import os
import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

##cwd = os.getcwd()
##print str(cwd)
folder = 'C:\Users\David\Documents\Recharge\Gauges\Sacramento'
os.chdir(folder)
files = os.listdir(folder)
cwd = os.getcwd()
print str(cwd)
print str(files)              


### Create list of data from CSV

for data in files:
    recs = []
    print str(data)
    fid = open(data)
    lines = fid.readlines()[0:]
    fid.close()
    rows = [line.split(',') for line in lines]
    for line in rows:

        try:  
            recs.append([datetime.datetime.strptime(line[2],'%m/%d/%Y'),  # date
            float(line[3])])  # discharge
        

        except ValueError:
            
            recs.append([datetime.datetime.strptime(line[2],'%m/%d/%Y'),  # date
            float(0.0)])  # discharge
##            
##            except ValueError:
##                recs.append([datetime.datetime.strptime(line[2],'%m/%d/%Y %H:%M'),  # date
##                float(0.0)])  # discharge

            
    print str(data)        
    print len(recs)
    lines = recs
    qAbo = np.array(lines)
    dateAbo = qAbo[:,0]
    qAbo = qAbo[:,1]
    print str(qAbo)
    name = os.path.splitext(data)[0]
    print name

    plt.figure(1,figsize=(20,8))
    plt.semilogy(dateAbo,qAbo,'g',markersize = 15,label = 'Discharge')
    plt.legend(loc=2)
    plt.title('Discharge at %s' % name)
    plt.xlabel('Date')
    plt.ylabel('Discharge [cfs]')
    plt.show()
    plt.close


    



