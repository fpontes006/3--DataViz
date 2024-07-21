import matplotlib.pyplot as plt

#1-  Dados Fictisios - Quantidade de Produtos Vendidos por vendedor

vendedores = ['Vendedor 1', 'Vendedor 2', 'Vendedor 3', 'Vendedor 4', 'Vendedor 5']
produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
quantidade = [10, 20, 30, 40, 50]

#2- Criando o Grafico de Barras
plt.figure(figsize=(10, 5))

plt.bar(
    vendedores,
    quantidade,
    color='b',
    label='Quantidade'
)

#3- Adicionando Legenda
plt.xlabel('Vendedores')
plt.ylabel('Quantidade')
plt.title('Quantidade de Produtos Vendidos por Vendedores')
plt.legend()
# plt.grid(True)

#4- Exibindo o Grafico
plt.show()