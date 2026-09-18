import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[10,20,30]
plt.plot(x1,y1,label="line1",color="g")
x2=[30,40,50]
y2=[30,40,50]
plt.plot(x2,y2,label="line2",color="b")
plt.title("2 line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()