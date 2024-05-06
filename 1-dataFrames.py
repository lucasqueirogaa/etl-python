import pandas as pd

df1 = pd.DataFrame({
    "idade": [13, 21, 32, 21, 16],
    "nome": ["Caio", "Rodrigo", "José", "Lucas", "Mateus"]
})

df2 = pd.DataFrame({
    "idade": [13, 21, 32, 21, 16],
    "nome": ["Caio", "Zulu", "João", "Igor", "Mateus"]
})


# dataframe1 = pd.DataFrame(dict1)

# print(dataframe1)

concat_df = pd.concat([df1, df2], ignore_index=True)

print(concat_df)
print(concat_df.drop_duplicates())
