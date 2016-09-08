## mosaic to new raster


import arcpy
from arcpy import env
arcpy.env.workspace = "C:\Recharge_GIS\UnzippedTar"
rasterList = arcpy.ListRasters()
rasterList.sort()
print str(rasterList)
firstRas = arcpy.Raster("sd8p0r0c0.tif")
for raster in rasterList:
    if "sd8" in raster:
        if "sd8p0r0c0.tif" not in raster:
            arcpy.MosaicToNewRaster_management(raster, firstRas,
                                               "landnew.tif", "World_Mercator.prj",
                                               "8_BIT_UNSIGNED", "40", "1", "LAST","FIRST")