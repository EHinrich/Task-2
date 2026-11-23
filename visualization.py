import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

V = 0.6
xi_0 = 0.0
gamma = 1.0 / np.sqrt(1 - V**2)

x = np.linspace(-15, 25, 500)
t_values = np.linspace(0, 20, 150)

def u_analytical(x, t):
    return 4 * np.arctan(np.exp(gamma * (x - V * t - xi_0)))

fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot([], [], lw=2, color='black', label=f'Кинк (V = {V})')

ax.set_xlim(x[0], x[-1])
ax.set_ylim(-0.5, 2 * np.pi + 0.5)
ax.set_yticks([0, np.pi, 2 * np.pi])
ax.set_yticklabels(['0', r'$\pi$', r'$2\pi$'])
ax.set_xlabel('x')
ax.set_ylabel('u(x, t)')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left')

def update(frame):
    t = t_values[frame]
    y = u_analytical(x, t)
    line.set_data(x, y)
    ax.set_title(f'Уравнение синус-Гордона, t = {t:.2f}')
    return line,

ani = FuncAnimation(fig, update, frames=len(t_values), interval=40, blit=False)

# ani.save('sine_gordon_kink.gif', writer='pillow', fps=25)

plt.show()
