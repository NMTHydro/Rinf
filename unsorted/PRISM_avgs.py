import arcpy
from arcpy import env

env.workspace = "C:\Recharge_GIS\PRISM_1981_2014.gdb"
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
rasterList = arcpy.ListRasters()
rasterList.sort()
print str(len(rasterList))

constant = 0.0
arcpy.env.workspace = "C:\Recharge_GIS\scratch.gdb"
outExtent = arcpy.Extent(266920,3869240,508520,4081240)
prevRas = arcpy.sa.CreateConstantRaster(constant,"FLOAT",4000,outExtent)


    
for year in range(1981,1982):
    print "Year " + str(year)
    
    for month in range(1,12):
        print "Month " + str(month)
        
        for raster in rasterList:
            
            print str(raster)
            
            filepath = arcpy.env.workspace = "C:\Recharge_GIS\Recharge_GIS\PRISM_1981_2014.gdb"
            
            if arcpy.Exists(filepath + "\PRISM_ppt_stable_4kmM2_" + str(year) + "0" + str(month) + "_bil"):

                    print 'found PRISM ' + str(year) + " month " + str(month)
                    
                    ras = arcpy.Raster(raster)
                    cumRas = prevRas + ras
                    prevRas = ras
                  
            elif arcpy.Exists(filepath + "\PRISM_ppt_stable_4kmM2_" + str(year) + str(month) + "_bil"):
                        
                    print 'found PRISM ' + str(year) + " month " + str(month)
                    
                    ras = arcpy.Raster(raster)
                    cumRas = prevRas + ras
                    prevRas = ras
            else:
                    print "Not Found"
                  
        cumPpt = cumRas    
        cumPpt.save("PRISM_ppt_annual_" + str(year))
                     
    print "Done year " + str(year)


        

