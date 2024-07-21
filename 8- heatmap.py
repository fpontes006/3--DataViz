import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1- Criando dados fictisios de preços de acoes
# Para diferentes empreses ao longo do trimestre

empresas = ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'Intel', 'Microsoft', 'NVIDIA', 'Qualcomm', 'Samsung', 'Twitter', 'Xiaomi']
trimestres = ['T1', 'T2', 'T3', 'T4']

dados = np.random.rand(12, 4) * 100
# Valores aleatorios de 0 a 100

# 2 -  Criando dataframe com os dados
df = pd.DataFrame(
    dados,
    columns=trimestres,
    index=empresas
)
# print(df)


# 3 - Criando heatmap usando o seaborn
plt.figure(figsize=(10, 5))
sns.heatmap(df, cmap='coolwarm', annot=True, fmt='.2f')
plt.title('Heatmap de Preços de Ações')
plt.xlabel('Trimestres')
plt.ylabel('Empresas')
plt.show()
