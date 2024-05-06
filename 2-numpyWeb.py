import pandas as pd
import numpy as np

df = pd.DataFrame({'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                   'acessos_app': [9, 34, None, None, 727, None, 1, 22, None, None, None],
                   'acessos_web': [None, 9834, 1, 19, 99, 102, None, None, 21, 87, None]})

# O numpy where vai criar uma nova coluna do df, através de uma verificação. Se o que tivermos nos 1º lugar for verdadeiro, retorna o que tivermos em 2º, se for falso, retorna o que tiver em 3º
# df['tem_app'] = np.where(df.acessos_app > 0, True, False)

# print(df)

df['tem_app_e_web'] = np.where((df.acessos_app > 0) & (df.acessos_web > 0), True, False)

print(df)
