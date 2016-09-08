  # Excel to Python for attractive time series plots
  # David Ketchum: 1 May 2015
  # ERTH 443 D. Cadol
  #
  #
  # This script will read .csv time series data, create a list (array) of time series data,
  # recognize the date and time of data, and plot it.
  #
  # See online matplotlib "http://matplotlib.org/index.html" to see examples with code of cool plot styles
  #
  # Step 1: save your .xlxs spreadsheet to .csv format in excel

import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

    
fid = open('C:\Users\David\Downloads\La_Selva_ET_data_DGK.csv', 'r')

  # Set the readlines to start from row 5, which is 4 in python in this case, so we don't read in the headers

lines = fid.readlines()[4:]
fid.close()
rows = [line.split(',') for line in lines]
print len(rows)


  # Step 2: On your .xlxs excel sheet go to file->excel options->formulas->R1 C1 reference style
  # Checking this will label your columns with numbers so you don't have to count the letters
  # Remember python lists start from 0!  So column 33 will be referred to as [32] in the code
  # Change the column numbers as you'd like to create a list with desired data

lines = [[datetime.datetime.strptime(line[0],'%m/%d/%Y %H:%M'), # line[0] is date
          float(line[2]),                                       # line[1] is stream discharge
          float(line[21]),                                      # line[2] is temp in C
          float(line[29]),                                      # line[3] is precip (mm)
          float(line[58]),                                      # line[4] is ASCE ET (mm)
          float(line[62]),                                      # line[5] is PT ET (mm)
          float(line[68]),
          float(line[37]),
          float(line[50])] for line in rows]                   # line[6] is PM ET (mm)

date = [line[0] for line in lines]
q = [line[1] for line in lines]
temp = [line[2] for line in lines]
ppt = [line[3] for line in lines]
asce = [line[4] for line in lines]
pT = [line[5] for line in lines]
print str(len(pT))
pM = [line[6] for line in lines]
cld = [line[7] for line in lines]
nrad = [line[8] for line in lines]
  # Calculate a trendline for a scatterplot of streamflow and PM ET
  # Adjust for apparent lag of about three hours
  # Select only daytime datas

date_day = []
q_minus = []
asce_adj = []
daytime = []
x = 0
for row in rows:
    x = x + 1
    tim = datetime.datetime.strptime(row[0],'%m/%d/%Y %H:%M')
    hr = tim.hour
    if hr in range(8,20):
        time = datetime.datetime.strptime(row[0],'%m/%d/%Y %H:%M')
        date_day.append(time)
        q_minus.append(q[x-7])
        asce_adj.append(asce[x])


##z = np.polyfit(q_minus,asce_adj,1)
##p = np.poly1d(z)
# corpmpt = np.corrcoef(q_minus,asce_adj)
# plt.scatter(q_minus,asce_adj,s=30,alpha=1,marker='o')
# # determine best fit line
# par = np.polyfit(q_minus, asce_adj, 1, full=True)
# slope=par[0][0]
# intercept=par[0][1]
# xl = [min(q_minus), max(q_minus)]
# yl = [slope*xx + intercept  for xx in xl]
# variance = np.var(asce_adj)
# residuals = np.var([(slope*xx + intercept - yy)  for xx,yy in zip(q_minus,asce_adj)])
# Rsqr = np.round(1-residuals/variance, decimals=2)
# cov = np.cov(q_minus,asce_adj)
# print str(cov)
# plt.text(.7*max(q_minus)+.1*min(q_minus),.7*max(asce_adj)+.1*min(asce_adj),'$R^2 = %0.2f$'% Rsqr, fontsize=20)
# plt.text(.4*max(q_minus)+.1*min(q_minus),.4*max(asce_adj)+.1*min(asce_adj),'$Covariance = %0.2f$'% cov[1][0], fontsize=20)
# plt.title('ASCE ET vs. Stream Discharge')
# plt.xlabel('Stream Discharge (cms)')
# plt.ylabel('ASCE ET (mm)')
# plt.show()

  # scatterplot of PM ET and stream discharge
# plt.plot(asce_adj,q_minus,'b*')
# plt.plot(p,'--r')
# plt.title('Penman-Montieth ET vs. Stream Discharge')
# plt.xlabel('Stream Discharge (cms)')
# plt.ylabel('ET (mm)')
# plt.show()


  # Step 3:  Choose the parameters you'd like to plot, go to the website for style ideas, you
  # can do a lot of different things, like error bars, histograms, etc.
time = []
ptEt = []
pmEt = []
asce_Et = []
precip = []
Q = []
for line in range (1,1608):
    ptEt.append(pT[line])
    pmEt.append(pM[line])
    asce_Et.append(asce[line])
    time.append(date[line])
    precip.append(ppt[line])
    Q.append(q[line])

fig, ax1 = plt.subplots(1,figsize=(15,5))
ax1.plot(time,precip,'b',label='Precipitation (mm)')
ax1.set_ylabel('Precipitation (mm)', color='k')
ax1.set_xlabel('Date')
# plt.ylim(0.0,30.0)
for tl in ax1.get_yticklabels():
    tl.set_color('b')
ax2 = ax1.twinx()
ax2.plot(time,Q,'g',label='Stream Discharge (mm)')
ax2.set_ylabel('Stream Discharge (cms)', color='k')
# plt.ylim(0.0,4.0)
for tl in ax2.get_yticklabels():
    tl.set_color('g')
for tl in ax2.get_xticklabels():
    tl.set_color('k')
plt.title('Precipitation and Stream Flow at La Selva Station (6 Mar - 14 Apr 2009)')
plt.show()
#
#   Take a some shorter time series to show the difference in the various ET estimation methods
#   This will be over a week
# time = []
# ptEt = []
# pmEt = []
# asce_Et = []
# precip = []
# q_minus = []
# x = 0
# cloud = []
# rad = []
# for line in range (1,168):
#     ptEt.append(pT[line])
#     pmEt.append(pM[line])
#     asce_Et.append(asce[line])
#     time.append(date[line])
#     precip.append(ppt[line])
#     q_minus.append(q[line])
#     cloud.append(cld[line])
#     rad.append(nrad[line])
#  calc correlation coeff and plot scatter
# corpmpt = np.corrcoef(q_minus,precip)
# plt.scatter(q_minus,precip,s=30,alpha=1,marker='.')
#  determine best fit line
# par = np.polyfit(q_minus, precip, 1, full=True)
# slope=par[0][0]
# intercept=par[0][1]
# xl = [min(q_minus), max(q_minus)]
# yl = [slope*xx + intercept  for xx in xl]
# variance = np.var(q_minus)
# residuals = np.var([(slope*xx + intercept - yy)  for xx,yy in zip(q_minus,precip)])
# Rsqr = np.round(1-residuals/variance, decimals=2)
# cov = np.cov(q_minus,precip,1)
# print str(cov)
# plt.text(.7*max(q_minus)+.1*min(q_minus),.95*max(precip)+.1*min(precip),'$R^2 = %0.2f$'% Rsqr, fontsize=20)
# plt.text(.7*max(q_minus)+.1*min(q_minus),1.05*max(precip)+.1*min(precip),'$Covariance = %0.2f$'% cov[1][0], fontsize=20)
# plt.title('Stream Discharge vs. ASCE ET (29 Mar - 8 Apr 2009')
# plt.xlabel('Stream Flow (cms))')
# plt.ylabel('ASCE ET (mm)')
# plt.show()
#
# plt.figure(2,figsize=(15,5))
# plt.plot(time,asce_Et,'-b',label = 'ASCE ET (mm)')
# plt.plot(time,precip,'-g',label = 'Precipitation (mm)')
# plt.plot(time,cloud,'-r',label = 'Cloudiness Function')
# plt.legend(loc=2)
# plt.title('Evapotranspiration at La Selva Station (25 Jan - 31 Jan 2009)')
# plt.xlabel('Time')
# plt.ylabel('ET (mm)')
# plt.show()
#

# Compare PM to discharge over each month
# time = []
# ptEt = []
# pmEt = []
# asce_Et = []
# q_Month = []
# for line in range (1,168):
#     ptEt.append(pT[line])
#     pmEt.append(pM[line])
#     asce_Et.append(asce[line])
#     q_Month.append(q[line])
#     time.append(date[line])
#
# print str(max(asce_Et))
# print str(max(q_Month))
# fig, ax1 = plt.subplots(1,figsize=(15,5))
# ax1.plot(time,asce_Et,'-r',label='Precipitation (mm)')
# ax1.plot(time,pmEt,'-r',label='Precipitation (mm)')
# ax1.plot(time,ptEt,'-r',label='Precipitation (mm)')
# ax1.set_ylabel('ET (mm)', color='k')
# plt.legend()
# ax1.set_xlabel('Time')
# plt.ylim(0.0,1.2)
# for tl in ax1.get_yticklabels():
#     tl.set_color('r')
# ax2 = ax1.twinx()
# ax2.plot(time,cloud,'-g',label='Net Radiation')
# ax2.set_ylabel('Net Radiation (MJ m-2 hr-1', color='k')
# plt.ylim(0.0,1.0)
# for tl in ax2.get_yticklabels():
#     tl.set_color('g')
# for tl in ax2.get_xticklabels():
#     tl.set_color('k')
# plt.title('ET and Net Radiation at La Selva Station (25 Jan - 31 Jan 2009)')
# plt.show()

