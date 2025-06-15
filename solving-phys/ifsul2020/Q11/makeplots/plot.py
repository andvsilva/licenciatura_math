import numpy as np
import matplotlib.pyplot as plt

# Definindo o tempo para o gráfico
t = np.linspace(0, 40, 500)  # Tempo de 0 a 40 segundos

# Posições do automóvel (aceleração de 1 m/s²)
x_A = 0.5 * t**2

# Posições da motocicleta (velocidade constante de 20 m/s)
x_M = 20 * t - 128

# Plotando o gráfico
plt.figure(figsize=(8,6))
plt.plot(t, x_A, label='Automóvel', color='blue')
plt.plot(t, x_M, label='Motocicleta', color='red', linestyle='--')


plt.scatter(0, 0, color='blue', zorder=5, label="Ponto Inicial do Automóvel")

# Marcando o ponto de interseção
plt.scatter(32, 512, color='black', zorder=5, label="Ponto de ultrapassagem")
plt.axvline(x=32, color='green', linestyle=':')
plt.axhline(y=20*32 - 128, color='green', linestyle=':')

plt.scatter(8, 32, color='green', zorder=5)
plt.axvline(x=8, color='green', linestyle=':')
plt.axhline(y=20*8 - 128, color='green', linestyle=':')

# Marcando os pontos específicos
plt.scatter(8, 32, color='black', zorder=5)  # Ponto (8, 32)
plt.scatter(32, 512, color='black', zorder=5)  # Ponto (32, 512)

plt.axhline(y=-128, color='purple', linestyle=':')
plt.scatter(0, -128, color='red', zorder=5, label="Posição inicial da motocicleta")


# Ajustes do gráfico
plt.title('Gráfico de Posição vs Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Espaço (m)')
plt.legend()
plt.grid(True)

plt.savefig('../images/grafico_posicao_tempo.pdf', format='pdf')

# Exibindo o gráfico
plt.show()
