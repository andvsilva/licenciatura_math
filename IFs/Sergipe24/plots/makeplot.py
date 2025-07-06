import numpy as np
import matplotlib.pyplot as plt

# Constantes
rho = 1     # densidade de carga arbitrária
epsilon_0 = 1  # constante de permissividade arbitrária
a = 1       # raio da esfera

# Função do campo elétrico
def E(r):
    E_vals = np.zeros_like(r)
    inside = r <= a
    outside = r > a
    E_vals[inside] = (rho * r[inside]) / (3 * epsilon_0)
    E_vals[outside] = (rho * a**3) / (3 * epsilon_0 * r[outside]**2)
    return E_vals

# Intervalo de r
r = np.linspace(0, 7*a, 500)
E_r = E(r)

# Gráfico
plt.figure(figsize=(8, 5))
plt.plot(r, E_r, label=r'$E(r)$', color='blue')
plt.axvline(a, color='gray', linestyle='--', label=r'$r = a$')
plt.title('Campo Elétrico $E(r)$ gerado por uma esfera uniformemente carregada')
plt.xlabel('r')
plt.ylabel(r'$E(r)$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('campo_eletrico_esfera.png', dpi=300)
plt.show()
