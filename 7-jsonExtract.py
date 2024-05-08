import pandas as pd

pd.set_option('display.max_columns', 500)

# Extração dos dados
acoes = pd.read_json('json/tb_acoes.json')
anos = pd.read_json('json/tb_anos.json')
orcamentos = pd.read_json('json/tb_orcamentos.json')
programas = pd.read_json('json/tb_programas.json')
unidades_orcamentarias = pd.read_json('json/tb_unidades_orcamentarias.json')

print(acoes.head())
print("===== Divisão ========")
print(anos.head())
print("===== Divisão ========")
print(orcamentos.head())
print("===== Divisão ========")
print(programas.head())
print("===== Divisão ========")
print(unidades_orcamentarias.head())
print("===== Divisão Para Merge Ações ========")

# Transformação dos dados
orcamentos = orcamentos.merge(acoes,
                              left_on='fk_acao',
                              right_on='id_acao',
                              how='left')

print(orcamentos.head())

print("===== Divisão Para Merge Programas ========")

orcamentos = orcamentos.merge(programas,
                              left_on='fk_programa',
                              right_on='id_programa',
                              how='left')

print(orcamentos.head())

print("===== Divisão Para Merge Unidades Orçamentárias ========")

orcamentos = orcamentos.merge(unidades_orcamentarias,
                              left_on='fk_unidade',
                              right_on='id_unidade',
                              how='left')

print(orcamentos.head())

print("===== Divisão Para Merge Anos ========")

orcamentos = orcamentos.merge(anos,
                              left_on='fk_ano',
                              right_on='id_ano',
                              how='left')

orcamentos.drop(columns=['id_acao', 'fk_acao'], inplace=True)
orcamentos.drop(columns=['id_programa', 'fk_programa'], inplace=True)
orcamentos.drop(columns=['id_unidade', 'fk_unidade'], inplace=True)
orcamentos.drop(columns=['id_ano', 'fk_ano'], inplace=True)

print(orcamentos.head())


