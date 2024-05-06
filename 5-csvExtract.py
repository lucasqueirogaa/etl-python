import pandas as pd
pd.set_option('display.max_columns', None)

olts = pd.read_csv('csv/OLTs.csv')
pops = pd.read_csv('csv/POPs.csv')

olts.rename(columns={'nome': 'nome_olt', 'id': 'id_olt'}, inplace=True)
pops.rename(columns={'nome': 'nome_pop', 'id': 'id_pop'}, inplace=True)
print(olts[:1])
pops_olts = olts.merge(pops, left_on='idPop', right_on='id_pop', how='left')

print(pops_olts[:3])
