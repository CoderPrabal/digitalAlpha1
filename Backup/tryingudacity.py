#!/usr/bin/python


print ("checking for nltk")
try:
    import nltk
except ImportError:
    print ("you should install nltk before continuing")

print ("checking for numpy")
try:
    import numpy
except ImportError:
    print ("you should install numpy before continuing")

print ("checking for scipy")
try:
    import scipy
except:
    print ("you should install scipy before continuing")

print ("checking for sklearn")
try:
    import sklearn
except:
    print ("you should install sklearn before continuing")

import urllib.request
url = "enron_mail_20150507.tar.gz"
#urllib.request.urlretrieve(url, filename="enron_mail_20150507.tar.gz") 
#print ("download complete!")


print()
print ("unzipping Enron dataset (this may take a while)")
import tarfile
import os
os.chdir("..")
tfile = tarfile.open(r"C:\\Users\\user\\.spyder-py3\\enron_mail_20150507.tar.gz", "r:tar")
tfile.extractall(".")

print ("you're ready to go!")

