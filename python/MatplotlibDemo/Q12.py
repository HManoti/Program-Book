import matplotlib.pyplot as plt
import numpy as np

dt=0.01
t=np.arange(0,10,dt)
nse=np.random.randn(len(t))
r=np.exp(-t/0.05)

cnse=np.convolve(nse,r)*dt
cnse=cnse[:len(t)]

#Default
s=0.1*np.sin(2*np.pi*t)+cnse
plt.subplot(211)
plt.title('Example 1:Default')
plt.plot(t,s)
plt.subplot(212)
plt.psd(s,512,1/dt)
plt.show()

s=0.1*np.sin(2*np.pi*t)+cnse
plt.subplot(211)
plt.title('Example 2:PSD change')
plt.plot(t,s)
plt.subplot(212)
plt.psd(s,256,1/dt)
plt.show()

s=0.1*np.sin(2*np.pi*t)+cnse
plt.subplot(211)
plt.title('Example 3:Colour change')
plt.plot(t,s)
plt.subplot(212)
plt.psd(s,512,1/dt,color='orange')
plt.show()

s=0.05*np.sin(2*np.pi*t)+cnse
plt.subplot(211)
plt.title('Example 4:Colour and Signal change')
plt.plot(t,s)
plt.subplot(212)
plt.psd(s,512,1/dt,color='purple')
plt.show()