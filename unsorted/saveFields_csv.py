
import matplotlib.pyplot as plt
import arcpy, os, sys
from arcpy import env
import numpy as np

arcpy.env.workspace = "C:\\Recharge_GIS\\Samples.gdb"
fc = "Sample_Sites_8JUN15"
cursor = arcpy.SearchCursor(fc)
field = "ETRM_pct"
ETRM_pct = [row.getValue(field) for row in cursor]
cursor = arcpy.SearchCursor(fc)
field = "PptAsRech_CMB_A"
CMB_pct = [row.getValue(field) for row in cursor]
cursor = arcpy.SearchCursor(fc)
field = "Location_Description"
name = [row.getValue(field) for row in cursor]
cursor = arcpy.SearchCursor(fc)
field = "Region"
region = [row.getValue(field) for row in cursor]
cursor = arcpy.SearchCursor(fc)
field = "Elev_m"
elev = [row.getValue(field) for row in cursor]
cursor = arcpy.SearchCursor(fc)
field = "PRISM_ppt_30yr_normal_4kmM2_"
precip = [row.getValue(field) for row in cursor]
print type(ETRM_pct)
print type(CMB_pct)
print type(name)

ETRM_pct = np.array(ETRM_pct,dtype=float)*100.0
CMB_pct = np.array(CMB_pct,dtype=float)
name = np.array(name,object)
region = np.array(region,object)
elev = np.array(elev,dtype=float)
precip = np.array(precip,dtype=float)

data = np.column_stack((region,name,elev,precip,ETRM_pct,CMB_pct))
print data

np.savetxt(('C:\\Users\\David\\Documents\\ArcGIS\\Data\\Csv\\RegNameElevETRM_CMB.csv'),
           data,fmt=['%s','%s','%1.3f','%1.3f','%1.3f','%1.3f'],delimiter=',')

##
##plt.scatter(CMB_pct[0:32],ETRM_pct[0:32],c='blue',marker=u'o',edgecolor='none')
##plt.title('Modeled Recharge vs. Chloride Mass Balance Recharge')
##plt.xlabel('CMB Recharge (Percent of Precipitation')
##plt.ylabel('ETRM Recharge(Perceent of Precipitation')
##plt.show()




  
    
