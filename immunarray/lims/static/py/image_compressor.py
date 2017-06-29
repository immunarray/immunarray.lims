#!/usr/bin/python
# -*- coding: utf-8 -*-
pass
import glob
import os,sys,gzip

"""filenames = glob.glob("/home/jpitts/Desktop/Images/*.tif")"""
folder = './'
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): 
        continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.tif', '.gz')
    print newname
    
"""f_out = gzip.open(new_name,'wb')
f_out.close()
f_in.close()

f_out = gzip.open('IA_R38.21_1_S001_Green.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()


filenames = glob.glob("/home/jpitts/Desktop/Images/*.tif")
for f in filenames:
    f_in = open(f, 'rb')
    f_out = gzip.open(f, 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()
"""
    
"""gzip.open(f, 'wb') as g;
        g.write()"""


