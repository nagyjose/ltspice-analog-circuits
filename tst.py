import numpy as np
import matplotlib.pyplot as plt

# Známý bod a směrnice
x0, y0 = 2, 3
m = 0.5  # směrnice

# Rozsah osy x, přes který vykreslíme přímku
x_vals = np.linspace(0, 10, 100)

# Vypočti odpovídající y podle rovnice přímky
y_vals = m * (x_vals - x0) + y0

# Vykreslení
plt.plot(x_vals, y_vals, 'r--', label=f'y = {m}(x - {x0}) + {y0}')
plt.plot(x0, y0, 'bo', label='Výchozí bod')  # výchozí bod

plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Přímka z bodu a směrnice')
plt.show()
