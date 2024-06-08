#Sub Plot
import matplotlib.pyplot as plt
names=['ram','amit','mudit']
marks=[87,50,98]

plt.figure(figsize=(9,3))

plt.subplot(131)
plt.bar(names,marks)

plt.subplot(132)
plt.scatter(names,marks)

plt.subplot(133)
plt.plot(names,marks)

plt.suptitle('Categorial Plotting')
plt.show()