#Standard Library
import pymysql  #database
import numpy       #mathematical operations
import matplotlib   #Graphs
import pandas       #Data Analysis

def show():
    print("Python")
def put():
    print("Hello")
import IImt2

from IImt2 import *
IImt2.show()
IImt2.put()

put= lambda x,y : x+y
print(put(4,5))