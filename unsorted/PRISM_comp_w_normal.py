import arcpy
from arcpy import env
import numpy as np
import matplotlib.pyplot as plt

env.workspace = "C:\Recharge_GIS\PRISM_1981_2014.gdb"
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

i = 0
for year in range(1981,2014):
    filepath = arcpy.env.workspace = "C:\Recharge_GIS\PRISM_1981_2014.gdb"
    if arcpy.Exists(filepath + "\\PRISM_ppt1_annual_" + str(year)):
        if i == 0:
            out_Ras = arcpy.Raster(filepath + "\\PRISM_ppt1_annual_" + str(year))
            i = 1
        else:
            print "Adding raster year: " + str(year)
            inras = arcpy.Raster(filepath + "\\PRISM_ppt1_annual_" + str(year))
            out_Ras = out_Ras + inras
            i = i + 1
            
avRas = out_Ras / i
print str(avRas)
print "i = " + str(i)

yr = []
maxm = []
minm = []
mean = []
std = []


for year in range(1981,2014):
    print "Year " + str(year)
    filepath = arcpy.env.workspace = "C:\Recharge_GIS\PRISM_1981_2014.gdb"
    if arcpy.Exists(filepath + "\\PRISM_ppt1_annual_" + str(year)):
        ras = arcpy.Raster(filepath + "\\PRISM_ppt1_annual_" + str(year))
        out_Ras = avRas - ras
        
        yr.append(year)

        desc = arcpy.GetRasterProperties_management(out_Ras, "MAXIMUM")
        print 'Max out_Ras value :   ' + str(desc)
        maxm.append(desc)
        desc = arcpy.GetRasterProperties_management(out_Ras, "MEAN")
        print 'Mean out_Ras value :   ' + str(desc)
        mean.append(desc)
        desc = arcpy.GetRasterProperties_management(out_Ras, "MINIMUM")
        print 'Min out_Ras value :   ' + str(desc)
        minm.append(desc)
        desc = arcpy.GetRasterProperties_management(out_Ras, "STD")
        print 'Std Dev out_Ras value :   ' + str(desc)
        std.append(desc)

        out_Ras.save(filepath + "\\PRISM_depFrom_Avg_" + str(year))

        
        print "Done year " + str(year)
        print ''


yr = np.array(yr,int)
maxm = np.array(maxm,float)
minm = np.array(minm,float)
mean = np.array(mean,float)
std = np.array(std,float)
avConst = np.sum(mean) / len(yr)
avConst = [avConst] * len(yr)


fig, ax1 = plt.subplots(1,figsize=(15,5))
ax1.plot(yr,mean,'g',label='Mean Precipitation (mm)')
ax1.plot(yr,maxm,'b',label='Max Precipitation')
ax1.plot(yr,minm,'r',label='Min Precipitation')
ax1.plot(yr,avConst,'--k',label='33 Year Average Precipitation')
ax1.set_ylabel('Precipitation (mm)', color='b')
ax1.set_xlabel('Date')
# plt.ylim(0.0,30.0)
for tl in ax1.get_yticklabels():
    tl.set_color('b')
ax2 = ax1.twinx()
ax2.plot(yr,std,'k*',label='Standard Deviation')
ax2.set_ylabel('Standard Deviation', color='k')
# plt.ylim(0.0,4.0)
for tl in ax2.get_yticklabels():
    tl.set_color('k')
for tl in ax2.get_xticklabels():
    tl.set_color('k')
plt.title('Annual Precipitation in New Mexico (1981 - 2013)')
plt.legend()
plt.show()

np.set_printoptions(precision = 4)
stats = np.column_stack((yr,maxm,minm,mean,std))
print "YEAR, MAX, MIN, MEAN, STD"  
print str(stats)


print "GIS will solve all our problems!"
                                 
