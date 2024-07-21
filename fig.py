import matplotlib.pyplot as plt
import numpy as np

# 1- Gerando dados aleatorios
x = np.arange(1,6)
y1 = np.array([1, 2, 3, 4, 5])
y2 = np.array([5, 4, 3, 2, 1])

# 2- Criando o subplots
fig, ax = plt.subplots(2,figsize=(10, 5))

#3- Criando o grafico de barras subplots superiores
ax[0].bar(x, y1, color='b')
ax[0].set_title('Grafico de barras superior')

#4- Criando o grafico de linhas subplots inferiores
ax[1].plot(x, y2,marker='o',linestyle='-', color='r')
ax[1].set_title('Grafico de linhas inferior')

# 5- Ajusta espacamento entre os subplots
plt.tight_layout()

plt.show()