import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4])

x = np.arange(0,12,1)
y = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y, label='sin', marker='o')
plt.plot(x,y2, label='cos', marker='x')
plt.title('sin graph')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.legend(loc=(0,0))

plt.xlim(0,max(x))

plt.show()