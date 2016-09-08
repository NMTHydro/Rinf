import arcpy
from arcpy import env
import ArcHydroTools

arcpy.CheckOutExtension("Spatial")

arcpy.env.overwriteOutput = True

arcpy.env.workspace = "C:\Recharge_GIS\fdr_all.gdb"

##desc = arcpy.Describe('C:\\Recharge_GIS\\fdr_all.gdb\\fdr_COb')
##print "Band Count:       %d" % desc.bandCount
##print "Compression Type: %s" % desc.compressionType
##print "Raster Format:    %s" % desc.format

rasterList = arcpy.ListRasters()
print str(rasterList)
clipped = []
for raster in rasterList:
    arcpy.Clip_management(raster,
                          "#",
                          "C:\Recharge_GIS\fdr_all.gdb\clp_" + raster,
                          "C:\Recharge_GIS\Display_Features.gdb\Headwaters",
                          "#",
                          "ClippingGeometry")
                 
                    


