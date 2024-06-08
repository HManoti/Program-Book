import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature=[36,12,34,24,5,56,1,3,66,7,8,99,23,89,76]

#plt.plot(days,temperature)

plt.plot(days,temperature,"ro--",linewidth=3,markersize=10)

#plt.axis([0,30,30,50])

plt.title("Delhi Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()