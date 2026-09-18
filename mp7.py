import matplotlib.pyplot as plt
import numpy as np
y1=[22,30,35,35,26]
y2=[25,32,30,35,29]
x=["G1","G2","G3","G4","G5"]
x1=np.arange(5)
w=0.40
plt.bar(x1-0.2,y1, width=w,color="g",label="men")
plt.bar(x1+0.2,y2, width=w,color="b",label="women")
plt.xticks(x1,x)
plt.title("score by group and gender")
plt.xlabel("person")
plt.ylabel("score")
plt.legend()
plt.show()