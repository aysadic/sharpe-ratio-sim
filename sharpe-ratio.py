from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

Rf = 0.01
Rx = 0.1
std_Rx = np.linspace(0.001,0.15,1000)
sharpeRatio = (Rx-Rf)/std_Rx

plt.plot(100*std_Rx,sharpeRatio,color='red')
plt.xlabel("Standard Deviation of Return [%]")
plt.ylabel("Sharpe Ratio")
plt.title("Sharpe Ratio for Rx=0.1, Rf=0.01")
plt.grid()
plt.show()
