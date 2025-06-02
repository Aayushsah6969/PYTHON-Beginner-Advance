import pandas as pd

data={
    'Name':['Aayush', 'Kumar', 'Sah'],
    'Marks':[23,45,56]
}
df = pd.DataFrame(data)
print(df.to_string(index=False))