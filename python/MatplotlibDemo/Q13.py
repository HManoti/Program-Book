import matplotlib.pyplot as plt
import numpy as np

ml_student_age=np.random.randint(18,45,(100))
py_student_age=np.random.randint(15,40,(100))

bins=[15,20,25,30,35,40,45]
plt.hist(ml_student_age,bins,rwidth=0.3,histtype="bar",orientation="vertical",color="r",label="ML Student")

plt.hist(py_student_age,bins,rwidth=0.3,histtype="bar",orientation="horizontal",color="g",label="Python Student")

plt.legend()
plt.show()