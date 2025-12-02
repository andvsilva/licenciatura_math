import numpy as np
import matplotlib.pyplot as plt

# função h(t) = 4t - t * 2^(0.2 t)
def h(t):
    return 4*t - t * (2**(0.2*t))

t = np.linspace(0, 12, 600)
y = h(t)

# raízes conhecidas: t=0 e t=10
roots_t = np.array([0.0, 10.0])
roots_y = h(roots_t)

plt.figure(figsize=(8,4.5))
plt.plot(t, y, label=r"$h(t)=4t - t\cdot 2^{0.2t}$")
plt.axhline(0, linewidth=1, linestyle="--", label=r"$y=0$")

# marcar raízes
plt.scatter(roots_t, roots_y, zorder=5)
for rt in roots_t:
    plt.annotate(f"{rt:.0f}", (rt, 0), textcoords="offset points", xytext=(5,8))

# preencher a região onde h(t)>0 (dolphin out of water)
mask = y > 0
plt.fill_between(t, y, where=mask, alpha=0.2)

plt.xlim(-0.5, 12)
plt.ylim(min(y)-1, max(y)+1)
plt.xlabel("t (s)")
plt.ylabel("h(t) (m)")
plt.title("Altura do golfinho no salto: $h(t)=4t - t\\cdot 2^{0.2t}$")
plt.legend()
plt.grid(True)

# salvar figura
filename = "../images/dolphin_jump_plot.png"
plt.savefig(filename, bbox_inches="tight", dpi=150)
plt.show()

print(f"[Download the image]({filename})")
