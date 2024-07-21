import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/Pedidos.csv")

# Grafico 1 - Quantidade de Unidades vendidas por regiao
plt.figure(figsize=(10, 5)) 
df.groupby("Regiao")["Unidades"].sum().plot(kind="bar", color="b")
plt.xlabel('Região')
plt.ylabel('Unidades')
plt.title('Quantidade de Unidades vendidas por Região')
plt.xticks(rotation=45)
plt.show()


# Grafico 2 - Distribuição das vendas por item (Pizza)
plt.figure(figsize=(10, 5))
df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das vendas por item')
plt.axis('equal')
plt.show()

# Grafico 3 - Relação entre preço unitário e quantidade vendida
plt.figure(figsize=(10, 5))
plt.scatter(df['PrecoUnidade'], df['Unidades'], color='b')
plt.xlabel('Precos Unitarios')
plt.ylabel('Quantidade Vendida')
plt.title('Relação entre Preco Unitário e Quantidade Vendida')
plt.grid(True)
plt.show()


# Grafico 4 - Quantidade de Unidades vendidas ao longo do Tempo
# Convertendo a coluna 'DataPedido' para o formato datetime
df['DataPedido'] = pd.to_datetime(df['DataPedido'])

plt.figure(figsize=(10, 5))
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line',marker='o', color='b')
plt.xlabel('Ano')
plt.ylabel('Unidades')
plt.title('Quantidade de Unidades vendidas ao longo do Tempo')
plt.grid(True)
plt.show()

# Grafico 5 - Quantidade de Unidades vendidas por Estado em cada regiao
pivot = df.pivot_table(index='Estado', columns='Regiao', values='Unidades', aggfunc='sum', fill_value=0)

plt.figure(figsize=(10, 5))
pivot.plot(kind='bar', stacked=True)
plt.xlabel('Estado')
plt.ylabel('Unidades')
plt.title('Quantidade de Unidades vendidas por Estado em cada regiao')
plt.legend(title='Regiao', loc='upper left', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45)
plt.show()

