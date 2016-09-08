import arcpy
from arcpy import env

env.workspace = "C:\Recharge_GIS\PRISM_1981_2014.gdb"
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True


i = 0   
for year in range(1981,2014):
    print "Year " + str(year)
    filepath = arcpy.env.workspace = "C:\Recharge_GIS\PRISM_1981_2014.gdb"
    arcpy.env.extent = arcpy.Extent(-109.294, 31.333, -103.000, 38.458)
    
    for month in range(1,13):
        print "Month " + str(month)
        
        if arcpy.Exists(filepath + "\\PRISM_ppt_stable_4kmM2_" + str(year) + "0" + str(month) + "_bil"):
            if i == 0:
                print 'found PRISM ' + str(year) + " month " + str(month)
                ras = arcpy.Raster(filepath + "\\PRISM_ppt_stable_4kmM2_" + str(year) + "0" + str(month) + "_bil")
                prevRas = ras
                i == 1
            else:
                print 'found PRISM ' + str(year) + " month " + str(month)
                ras = arcpy.Raster(filepath + "\\PRISM_ppt_stable_4kmM2_" + str(year) + "0" + str(month) + "_bil")
                cumRas = arcpy.sa.Plus(prevRas,ras)
                prevRas = ras
              
        if arcpy.Exists(filepath + "\\PRISM_ppt_stable_4kmM2_" + str(year) + str(month) + "_bil"):
                    
                print 'found PRISM ' + str(year) + " month " + str(month)
                
                ras = arcpy.Raster(filepath + "\\PRISM_ppt_stable_4kmM2_" + str(year) + str(month) + "_bil")
                cumRas = arcpy.sa.Plus(prevRas,ras)
                prevRas = ras
        else:
                print "Not Found"
                  
    cumPpt = cumRas    
    # cumPpt.save(filepath + "\\PRISM_ppt1_annual_" + str(year))
    print "Done year " + str(year)

time = []
ptEt = []
pmEt = []
asce_Et = []
precip = []
Q = []
for line in range (1536,1608):
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
plt.ylim(0.0,30.0)
for tl in ax1.get_yticklabels():
    tl.set_color('b')
ax2 = ax1.twinx()
ax2.plot(time,Q,'g',label='Stream Discharge (mm)')
ax2.set_ylabel('Stream Discharge (cms)', color='k')
plt.ylim(0.0,4.0)
for tl in ax2.get_yticklabels():
    tl.set_color('g')
for tl in ax2.get_xticklabels():
    tl.set_color('k')
plt.title('Precipitation and Stream Flow at La Selva Station (6 Mar - 14 Apr 2009)')
plt.show()
        

