import pandas as pd
data={"name":['a','b','c','d','e'],
      "occupation":['A1','A1','A1','B1','B1'],
      "salary":[20,30,40,27,23]}
df=pd.DataFrame(data)
print(df.to_string())
occ_avg=df.groupby('occupation')['salary'].mean()
print("avg salary per occupation")
print(occ_avg.to_string())