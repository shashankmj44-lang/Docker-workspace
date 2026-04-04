import sys
print("arguments",sys.argv)
print("hello world ")
month=int(sys.argv[1])
print(f" month is {month}")

import pandas as pd

data={"A":[1,2],"B":[3,4]}
df=pd.DataFrame(data)
df.to_parquet(f"output_{month}.parquet")