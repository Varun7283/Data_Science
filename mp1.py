import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y,marker="o",color="r",mec="g",mfc="g",linestyle="dotted")
plt.title("simple line plot",color="g")
plt.xlabel("x axis",color="r")
plt.ylabel("y axis",color="r")
plt.show()