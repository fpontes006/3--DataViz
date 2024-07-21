import matplotlib.pyplot as plt

# 1- Dados Fictisios - Vendas ao longo dos Meses

meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
vendas = [2500, 2900, 1500, 2150, 1700, 2200, 3400, 2900, 5000, 4100, 4500, 2000]

# 1- Criando o Grafico de Linha

plt.figure(figsize=(10, 5))
plt.plot(
    meses,
    vendas,
    marker='o',
    linestyle='-',
    color='b',
    label='Vendas'
)

#3- Adicionando Legenda
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Vendas ao longo dos meses')
plt.legend()
plt.grid(True)

#4- Exibindo o Grafico
plt.show()