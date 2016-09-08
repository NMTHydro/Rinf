import arcpy
import tempfile
import os
import shutil

sourceImage = "E:\PRISM\Precip\800m\Daily\1984x\PRISM_NM_19840101.tif"
inputImage = "E:\PRISM\Temp\Maximum\Unclipped\1984\cai_tmax_us_us_30s_19840101.bil"
outputFilename = "E:\PRISM\Temp\Maximum\1984\cai_tmax_us_us_30s_19840101.tif"

# Snap to source image and source image extent
arcpy.env.extent = sourceImage
arcpy.env.snapRaster = sourceImage

# Get cell size
cellx = arcpy.GetRasterProperties_management(sourceImage, "CELLSIZEX")

# Get temporary directory and filename
tempDir = tempfile.mkdtemp()
tempFilename = 'E:/subset/test/' + basename(outputFilename) +'_proj.tif'

# Reproject
arcpy.ProjectRaster_management(inputImage,tempFilename,sourceImage, "#", cellx)

#
# Clip to source file
#

# Get envelope for clipping
top = arcpy.GetRasterProperties_management(sourceImage, "TOP")
left = arcpy.GetRasterProperties_management(sourceImage, "LEFT")
bottom = arcpy.GetRasterProperties_management(sourceImage, "BOTTOM")
right = arcpy.GetRasterProperties_management(sourceImage, "RIGHT")
envelope = str(left) + ' ' + str(bottom) + ' '+ str(right) + ' ' + str(top)

# Clip and save
clipr = arcpy.Clip_management(tempFilename, envelope, outputFilename, sourceImage,"#","NONE")
filePath = "E:\PRISM\temporary"
env.workspace = filePath
clipr.save(filePath + "\\" + "tmax_us_us_30s_19840101.tif")
