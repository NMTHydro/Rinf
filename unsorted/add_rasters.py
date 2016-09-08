import gzip, os, shutil

inPath = 'C:\Users\David\Downloads\d8Slope.tar.gz'
outPath = 'C:\Users\David\Downloads\d8Slope.tar'

for File in os.listdir(inPath):
    print 'Unzipping: ' + File[:-3]
    inF = gzip.open(os.path.join(inPath, File), 'rb')
    outF = open(os.path.join(outPath, File[:-3]), 'wb')
    shutil.copyfileobj(inF,outF)
    inF.close()
    outF.close()