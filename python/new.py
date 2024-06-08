import matplotlib.pyplot as plt
from pandas import read_csv

filename= 'abc.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']

data=read_csv(filename,names=names)
data.hist()
plt.show()