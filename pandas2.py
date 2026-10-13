import pandas as pd
data = [['Geek1', 28, 'Analyst'], ['Geek2', 35, 'Manager'], ['Geek3', 29, 'Developer']]
columns = ['Name', 'Age', 'Occupation']
df = pd.DataFrame.from_records(data, columns=columns)
print(df)