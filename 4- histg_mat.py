import matplotlib.pyplot as plt
import numpy as np

# 1- Gerando dados aleatorios - Pontuaçoes de um teste
pontos = np.random.randint(50, 100, 100)

# 2- Criando o grafico de Histograma
plt.figure(figsize=(10, 5))
plt.hist(pontos, bins=10, color='b', label='Pontos')
plt.xlabel('Pontos')
plt.ylabel('Quantidade')
plt.title('Histograma de Pontos')
plt.legend()
# plt.grid(True)
plt.show()