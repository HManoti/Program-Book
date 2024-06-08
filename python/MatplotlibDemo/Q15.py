import matplotlib.pyplot as plt
from pandas import read_csv

filename='company_sales_data.csv'
names=['month_number','facecream']

data=read_csv(filename,names=names)
data.plot(kind='density',subplots=True,layout=(3,3),sharex=False)

plt.show()