import pandas as pd
df = pd.read_csv('students.csv', delimiter = ',',na_values="nan")

print(df)