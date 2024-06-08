import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,2,3,4,5], 'go-', label='line 1',linewidth=5)

plt.plot([1,2,3,4,5],[1,4,9,16,25],'rs-',label='line 2')

plt.axis([-2,6,0,25])     #range of x and y axis
plt.legend()   #label display
plt.show()
