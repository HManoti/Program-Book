#working with Files

#C:\Users\anvia\Desktop
x=open("GITS.txt","a") #w,w+,a
x.write("\ntumpe hum to mare jaa rhe h")

#C:\Users\anvia\Desktop
x=open("A.txt","w") #w,w+,a
x.write("\ntumpe hum to mare jaa rhe h")

import shutil
shutil.copyfile("GITS.txt","A.txt")      #copy content one to another file

#Rename a file from t.txt to t2.txt
import os
os.rename("GITS.txt","h.txt")



