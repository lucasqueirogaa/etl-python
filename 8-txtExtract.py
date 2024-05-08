import pandas as pd
import numpy as np

df = pd.read_csv('txt/NYNEWYOR.txt', delim_whitespace=True, header=None)
df.rename(columns={
    0: 'month',
    1: 'day',
    2: 'year',
    3: 'temp'
}, inplace=True)

print(len(df[df.temp == -99]))

df.temp = df.temp.replace(-99, np.nan)

print(len(df[df.temp == -99]))

df['elemento_anterior'] = df.temp.shift(1)
df['elemento_posterior'] = df.temp.shift(-1)
df['back_fill'] = df.temp.bfill(axis=0)
df['foward_fill'] = df.temp.ffill(axis=0)

print(df.head())

df['substituicao'] = (df.temp.shift(1).ffill(axis=0) + df.temp.shift(-1).bfill(axis=0) / 2)

df.temp = np.where(df.temp.notnull() == False, df.substituicao, df.temp)

print(f"Agora nóes temos {len(df[df.temp.notnull() == False])} nulos")

df['temp_celcius'] = (df.temp - 32) * (5/9)
