import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 1- Gerendo dados aleatorios
x = np.random.randn(50)
y = np.random.randn(50)

# 2- Criando o grafico de Dispersão
plt.figure(figsize=(10, 5))
plt.scatter(x, y, marker='o', color='b', label='Dispersão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Grafico de Dispersão')
plt.legend()
plt.grid(True)
plt.show()

#3- criando grafico 3D
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, marker='o', color='b', label='Dispersão')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
ax.set_title('Grafico 3D')
ax.legend()
plt.grid(True)
plt.show()

