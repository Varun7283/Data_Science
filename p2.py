import pandas as pd
sr = pd.Series(pd.date_range(start="2021-05-01", end="2021-05-12" , freq="D"))
print(sr.to_string(index=False))