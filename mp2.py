import matplotlib.pyplot as plt
import pandas as pd
data=({"T":[12,14,16,18,20,22,24],
       "S":[100,200,250,400,300,450,500]})
df=pd.DataFrame(data)
plt.plot(df["T"],df["S"],marker="o")
plt.title("Temperature-Sales",color="g")
plt.xlabel("temperature",color="r")
plt.ylabel("sales",color="r")
plt.show()