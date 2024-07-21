import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px

# 1 - Carregar o dataset Diamonts
diamonds = sns.load_dataset('diamonds')

# print(diamonds)

# 2 - Criando grafico de disperção interativo com Plotly

fig = px.scatter(
    diamonds,
    x="carat", 
    y="price", 
    color="cut", 
    size='depth',
    hover_data=['x', 'y'],
    title='Disperção de Diamantes: Peso vs Preço'
)

fig.show()
