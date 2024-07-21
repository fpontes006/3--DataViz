import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1 - Craiando um dataframe ficticio
data = {
    'Preco': [20,25,30,18,22],
    'Quantidade': [100,120,140,160,180],
    'Receita': [2000,2500,3000,2800,3200]
}

df = pd.DataFrame(data)
# print(df)

#2 - Criando pairplot
sns.set(style="ticks")
sns.pairplot(df, diag_kind='kde')
plt.suptitle('Relacoes entre Preço,Quantidade e Receita', y=1.02)
plt.show()