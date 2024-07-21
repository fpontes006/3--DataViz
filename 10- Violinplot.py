import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1 - Criando dados ficticios
caracteristicas = ['Caracteristica 1', 'Caracteristica 2', 'Caracteristica 3', 'Caracteristica 4']
vendas = {
    'Categoria': np.random.choice(caracteristicas, 1000),
    'vendas': np.random.normal(loc=50, scale=20, size=1000) 
}

df=pd.DataFrame(vendas)
# print(df)

# 2- Criando Violinplot com seaborn
plt.figure(figsize=(10, 5))
sns.violinplot(x='Categoria', y='vendas', data=df,palette='muted')
plt.title('Violinplot')
plt.xlabel('Caracteristicas')
plt.ylabel('Vendas')
plt.show()