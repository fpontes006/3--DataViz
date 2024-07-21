import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("data/Pedidos.csv")

# 1- Criando uma unica figura com quatro graficos
fig, ax = plt.subplots(2, 2, figsize=(15, 15))

# Grafico 1 - Quantidade de Unidades vendidas por regiao
df.groupby("Regiao")["Unidades"].sum().plot(kind="bar", color="b",ax=ax[0, 0])
ax[0, 0].set_xlabel('Região')
ax[0, 0].set_ylabel('Unidades')
ax[0, 0].set_title('Quantidade de Unidades vendidas por Região')
ax[0, 0].tick_params(axis='x',rotation=45)


# Grafico 2 - Distribuição das vendas por item (Pizza)
df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90,ax=ax[0, 1])
ax[0, 1].set_title('Distribuição das vendas por item')
ax[0, 1].axis('equal')

# Grafico 3 - Relação entre preço unitário e quantidade vendida
ax[1, 0].scatter(df['PrecoUnidade'], df['Unidades'], color='b')
ax[1, 0].set_xlabel('Precos Unitarios')
ax[1, 0].set_ylabel('Quantidade Vendida')
ax[1, 0].set_title('Relação entre Preco Unitário e Quantidade Vendida')
ax[1, 0].grid(True)

# Grafico 4 - Quantidade de Unidades vendidas ao longo do Tempo
# Convertendo a coluna 'DataPedido' para o formato datetime
df['DataPedido'] = pd.to_datetime(df['DataPedido'])

plt.figure(figsize=(10, 5))
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line',marker='o', color='b',ax=ax[1, 1])
ax[1, 1].set_xlabel('Ano')
ax[1, 1].set_ylabel('Unidades')
ax[1, 1].set_title('Quantidade de Unidades vendidas ao longo do Tempo')
ax[1, 1].grid(True)




plt.tight_layout()
plt.show()