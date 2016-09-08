from os import listdir
from os.path import isfile, join
mypath = "C://Recharge_GIS//fdr_all.gdb"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print str(onlyfiles)
##
##fileList = listdir("C:\Recharge_GIS\fdr_all.gdb")
##print str(fileList)
