import pandas as pd

df = pd.read_csv('data/math.csv')

df_new = df[df['Number Tested'] > 20]
#print(df_new['Number Tested'].head(10))

inspect = df_new.isna().sum()
#print(inspect)

df_new.to_csv('data/clean_data.csv')  