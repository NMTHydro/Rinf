import os

path = "C:\\Recharge_GIS\\newNDVI\\2001"
os.chdir(path)

## make an index, rename
i = 0
b = []
## rename .tif
for obj in range(1,24):
    if obj == 23:
        a = i + 1
        i = a + 12
##        print str(obj)+ " Start: " + str(a)
##        print str(obj)+ " End: " + str(i)
##        os.rename((path + "\\2001_" + str(obj) + ".tif"),(path + "\\2001_" + str(a) + "_" + str(i) + ".tif"))
        b.append(a)
        break
    a = i + 1
    i = a + 15
##    print str(obj)+ " Start: " + str(a)
##    print str(obj)+ " End: " + str(i)
    b.append(a)
print b
##    os.rename((path + "\\2001_" + str(obj) + ".tif"),(path + "\\2001_" + str(a) + "_" + str(i) + ".tif"))
##
#### rename .aux
##i = 0
##for obj in range(1,24):
##    if obj == 23:
##        a = i + 1
##        i = a + 12
##        print str(obj)+ " Start: " + str(a)
##        print str(obj)+ " End: " + str(i)
##        os.rename((path + "\\2001_" + str(obj) + ".aux"),(path + "\\2001_" + str(a) + "_" + str(i) + ".aux"))
##        break
##    a = i + 1
##    i = a + 15
##    print str(obj)+ " Start: " + str(a)
##    print str(obj)+ " End: " + str(i)
##    os.rename((path + "\\2001_" + str(obj) + ".aux"),(path + "\\2001_" + str(a) + "_" + str(i) + ".aux"))    
##
#### rename .rrd
##i = 0
##for obj in range(1,24):
##    if obj == 23:
##        a = i + 1
##        i = a + 12
##        print str(obj)+ " Start: " + str(a)
##        print str(obj)+ " End: " + str(i)
##        os.rename((path + "\\2001_" + str(obj) + ".rrd"),(path + "\\2001_" + str(a) + "_" + str(i) + ".rrd"))
##        break
##    a = i + 1
##    i = a + 15
##    print str(obj)+ " Start: " + str(a)
##    print str(obj)+ " End: " + str(i)
##    os.rename((path + "\\2001_" + str(obj) + ".rrd"),(path + "\\2001_" + str(a) + "_" + str(i) + ".rrd"))
