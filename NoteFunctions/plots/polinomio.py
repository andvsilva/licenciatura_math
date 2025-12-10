import numpy as np
import matplotlib.pyplot as plt

# Define a função
def h(x):
    return x / (x + 1)

# Cria o intervalo (evitando x = -1 para não dar divisão por zero)
x = np.linspace(-3, 0.5, 400)
x = x[x != -1]

# Calcula h(x)
y = h(x)

# Plota
plt.plot(x, y)
plt.axvline(-1, color='red', linestyle='--', label='Assíntota x = -1')
plt.axhline(1, color='green', linestyle='--', label='Assíntota y = 1')

plt.xlabel("x")
plt.ylabel("h(x)")
plt.title("Gráfico de h(x) = x/(x+1)")
plt.legend()
plt.grid(True)
plt.ylim(-50, 50)

plt.show()
