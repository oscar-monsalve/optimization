import numpy as np
import matplotlib.pyplot as plt


def lifeguard_time(x: list) -> list:
    return (1/7 * (np.sqrt(50**2 + x**2))) + (0.5 * (np.sqrt(50**2 + (100-x)**2)))


x = np.linspace(0, 100, 100)
y = lifeguard_time(x)

# Find the minimum y value and the corresponding x value
min_index = np.argmin(y)
optimum_x = x[min_index]
min_y = y[min_index]

plt.plot(x, y, label='Lifeguard Time')
plt.scatter(optimum_x, min_y, color='red', zorder=5)  # Adding the point
plt.annotate(f'Min Time: {min_y:.2f}\nat x: {optimum_x:.2f}', xy=(optimum_x, min_y),
             xytext=(optimum_x-5, min_y+5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=8)

plt.xlabel('x (m)')
plt.ylabel(r'Time $t$ (s)')
plt.title('Lifeguard Time vs. Distance')
plt.legend()
plt.grid(True)
plt.show()
