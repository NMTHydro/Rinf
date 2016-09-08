import arcpy
from arcpy import env

env.workspace = "C:\Recharge_GIS\PRISM.gdb"
print "extent set"
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True


rasterList = arcpy.ListRasters()
rasterList.sort()
print str(rasterList)

for raster in rasterList:
    env.workspace = "C:\Recharge_GIS\Datatest.gdb"
    clip = arcpy.clip_management(raster,"",raster + "_clip","Headwaters","0","MAXOF")
    print "clipped " + str(raster)
                                 
    
