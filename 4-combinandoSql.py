import pandas as pd
from pandasql import sqldf

categories = pd.read_csv('categories.csv')
products = pd.read_csv('products.csv')

query = """ 
    SELECT
        p.id as product_id,
        p.name as product_name,
        p.price,
        c.name as category_name
    FROM products p
    JOIN categories c on c.id = p.category_id
"""

resultado = sqldf(query)
print(resultado)
