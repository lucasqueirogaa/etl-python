import pandas as pd

df = pd.DataFrame({'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'name': ['Camiseta', 'Geladeira', 'Calça', 'Fogão', 'Enciclopédia', 'Bíblia',
                            'Perfume', 'Meia', 'Microondas', 'TV']})

df['categoria'] = df['name'].apply(lambda x: 'Eletrodoméstico' if x in ["Fogão", "Microondas", "TV"] else (
    'Vestuário' if x in ["Camiseta", "Calça", "Meia"] else (
        'Livro' if x in ["Enciclopédia", "Bíblia"] else "Outros"
    )
))

print(df)
