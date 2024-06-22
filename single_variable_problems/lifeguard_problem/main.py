import numpy as np
import matplotlib.pyplot as plt


def lifeguard_time(x: list) -> list:
    return (1/7 * (np.sqrt(50**2 + x**2))) + (0.5 * (np.sqrt(50**2 + (100-x)**2)))


x = np.linspace(0, 100, 100)
y = lifeguard_time(x)

min_time = np.min(y)

index = y.index(min_time)

print(f"x: {x[index]}, y: {min_time}")

plt.plot(x, y)
plt.show()
