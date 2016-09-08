import os
import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

##cwd = os.getcwd()
##print str(cwd)
folder = 'C:\Users\David\Documents\Recharge\Gauges\Gauge_Data_HF_csv'
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
        recs.append([datetime.datetime.strptime(line[2],'%m/%d/%Y %H:%M'),  # date
        float(line[6])])  # discharge


    print str(data)
    print len(recs)
    lines = recs
    lines = np.array(lines)
    date = lines[:,0]
    q = lines[:,1] * 86400/35.31467

    # name = os.path.splitext(data)[0]
    # print name

    plt.figure(1,figsize=(20,8))
    plt.semilogy(date,q,'r',markersize = 15,label = 'Discharge')
    # plt.semilogy(date,ppt,'g',markersize = 15,label = 'Precipitation')
    plt.legend(loc=2)
    plt.title('Discharge at Rio Pueblo de Taos, 08269000,  15 Minute Interval')
    plt.xlabel('Date')
    plt.ylabel('Discharge [cfs]')
    plt.show()


    



