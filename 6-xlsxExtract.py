import pandas as pd

atletas = pd.read_excel("xlsx/Athletes.xlsx")
treinadores = pd.read_excel("xlsx/Coaches.xlsx")
ent_genereos = pd.read_excel("xlsx/EntriesGender.xlsx")
medalhas = pd.read_excel("xlsx/Medals.xlsx")
times = pd.read_excel("xlsx/Teams.xlsx")

print(atletas.NOC.nunique(),
      atletas.Discipline.nunique())  # Verificação de quantas informações únicas tem em cada coluna
print(f"Nós temos {len(atletas)} itens em atletas")

# Atléticas por modalidade por país
atletas_discipline = atletas.groupby(['NOC', 'Discipline'])['Name'].nunique()
atletas_to_df = pd.DataFrame(atletas_discipline).reset_index().rename(columns={
    'Name': 'numero_atletas',
    'Discipline': 'modalidade',
    'NOC': 'pais'
})

print(atletas_to_df)

print("========DIVISION========")

# Treinadores

treinadores_discipline = treinadores.groupby(['NOC', 'Discipline'])['Name'].nunique().reset_index().rename(columns={
    'Name': 'numero_treinadores',
    'Discipline': 'modalidade',
    'NOC': 'pais'
})

print(treinadores_discipline)

print("========DIVISION========")

# Times por disciplina por país

times['categoria'] = times.Event.apply(lambda x: 'Masculino' if 'Men' in x else ('Feminino' if 'Women' in x else ('Misto' if 'Mixed' in x else 'Outros')))

print(times.head())
print(times.categoria.value_counts())

times_masc = pd.DataFrame(times[times.categoria == 'Masculino'].groupby(['NOC', 'Discipline'])['Name'].nunique().reset_index().rename(columns={
    'Name': 'times_masculinos',
    'Discipline': 'modalidade',
    'NOC': 'pais'
}))
times_fem = pd.DataFrame(times[times.categoria == 'Feminino'].groupby(['NOC', 'Discipline'])['Name'].nunique().reset_index().rename(columns={
    'Name': 'times_femininos',
    'Discipline': 'modalidade',
    'NOC': 'pais'
}))
times_misto = pd.DataFrame(times[times.categoria == 'Misto'].groupby(['NOC', 'Discipline'])['Name'].nunique().reset_index().rename(columns={
    'Name': 'times_mistos',
    'Discipline': 'modalidade',
    'NOC': 'pais'
}))
times_outros = pd.DataFrame(times[times.categoria == 'Outros'].groupby(['NOC', 'Discipline'])['Name'].nunique().reset_index().rename(columns={
    'Name': 'outros_times',
    'Discipline': 'modalidade',
    'NOC': 'pais'
}))

print("=====> Times Masculino")
print(times_masc.head())
print("=====> Times Femininos")
print(times_fem.head())
print("=====> Times Mistos")
print(times_misto.head())
print("=====> Times Outros")
print(times_outros.head())






