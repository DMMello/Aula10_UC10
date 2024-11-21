#pip install pandas sqlalchemy pymysql
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

host = 'localhost'
user = 'root'
password = 'root'
database = 'db_loja'

# Criação da conexão com o banco de dados
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Leitura dos dados da tabela de produtos (com uma consulta SQL)
df_estoque = pd.read_sql('SELECT * FROM tb_produtos', engine)
# print(df_estoque.columns)

# Calcula o valor de estoque por linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']
# print(df_estoque)
# print(30 * '*')

#agrupando os protudos com o mesmo nome e somando as quantidades e valores
df_agrupado = df_estoque.groupby('NomeProduto').agg({'QuantidadeEstoque':'sum','TotalEstoque': 'sum'}).reset_index()
# print(df_agrupado)

# # Calcula o valor total geral em estoque
# print(f"Total geral em estoque: R$ {df_estoque['TotalEstoque'].sum()}")
# print(20 * '*')

# # Calcula a mediana da coluna 'Valor' (pode ser alterado para 'TotalEstoque' se necessário)
# mediana = np.median(df_estoque['TotalEstoque'])
# print(f"A mediana dos valores é: R$ {mediana:.2f}")
# print(20 * '*')

# # Calcula a mediana da coluna 'Valor' (pode ser alterado para 'TotalEstoque' se necessário)
# media = np.mean(df_estoque['TotalEstoque'])
# print(f"A media dos valores é: R$ {media:.2f}")
# print(30 * '/')
# print(30 * '/')

# #transformando o campo TotalEstoque em um array numpy
# array_total_estoque = np.array(df_estoque['TotalEstoque'])
# # print(array_total_estoque)
# media = np.mean(array_total_estoque)
# mediana = np.median(array_total_estoque)
# print(f"A media dos valores é: R$ {media:.2f}")
# print(f"A mediana dos valores é: R$ {mediana:.2f}")

# distancia = abs((media - mediana)/mediana) *100
# print(distancia)

#ordenando os produtos pelo total de estoque
df_ordenado= df_agrupado.sort_values(by='TotalEstoque', ascending=False)

#exibindo os produtos agrupados com o total de estoque
print(df_ordenado[['NomeProduto','TotalEstoque']])

#calculando o total geral do estoque
print(f'\nTotal geral em estoque: R$ {df_ordenado["TotalEstoque"].sum()}')