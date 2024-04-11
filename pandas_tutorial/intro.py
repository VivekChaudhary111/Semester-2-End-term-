# pandas : data visualisation tool
import pandas as pd
series = pd.Series([62, 40, 22, 48], index=list('abcd'))
print(series[1:3])

# syntax for DataFrame visualization
# pandas.DataFrame(data, index, columns, dtype, copy)
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
print()

# Through Dictionary
data1 = {'Name':['Alex','Bob','Clarke'], 'Age':[10, 12, 13]}
df1 = pd.DataFrame(data1)
print(df1)
