import matplotlib.pyplot as plt

#Pie chart where the slices will be ordered and plotted

student='ram','alok','alina','heena'
per=[45,30,15,10]
explode=(0.1,0,0,0)

figl,axl=plt.subplots()
axl.pie(per,explode=explode, labels=student, autopct='%1.1f%%',shadow=True,startangle=90)
axl.axis('equal')      
plt.show()