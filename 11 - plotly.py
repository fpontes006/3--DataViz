import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

# 1 - Criando Dados Ficticios
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'StockA': [100 + i for i in range(100)],
    'StockB': [120 - i for i in range(100)],
    'Stockc': [90 + (i * 0.5) for i in range(100)]
}

df = pd.DataFrame(data)
# print(df)

# 2 - Criando o grafico de linhas interativos Plotly

fig = go.Figure()

fig.add_trace(go.Scatter(
    x= df['Date'],
    y= df['StockA'],
    mode='lines',
    name = 'Stock A'
))
fig.add_trace(go.Scatter(
    x= df['Date'],
    y= df['StockB'],
    mode='lines',
    name = 'Stock B'
))
fig.add_trace(go.Scatter(
    x= df['Date'],
    y= df['Stockc'],
    mode='lines',
    name = 'Stock C'
))

# 3 - layouit do grafico

fig.update_layout(
    title='Variação de preço ao longo do Tempo',
    xaxis_title = 'Data',
    yaxis_title='Preço',
    hovermode='x'
)
fig.show()