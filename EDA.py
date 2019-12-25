import pandas as pd
df = pd.read_csv('audio_data_new.csv')
df2 = pd.read_csv('audio_data.csv')
df_new = pd.concat([df,df2])
# check for duplicated rows 
# print(pd.concat(g for _, g in df_new.groupby("id") if len(g) > 1))
df_new = df_new.drop_duplicates(subset = ['id'], keep = 'first')
print(len(df_new))


#check for null values
# print(df_new.isnull().sum())
df_new= df_new.dropna()
# print(df_new.isnull().sum())

print(df_new.groupby(['genre']).size())
df_new.to_csv('audio_data_newer.csv')
#there are 360 null values of preview urls.... need to recollect data
