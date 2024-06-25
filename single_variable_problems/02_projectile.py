# Projectile considering air friction (aerodynamic drag)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dSdt(t: list, S: list) -> list:
    x, vx, y, vy = S

    # Define constants
    g = 9.81  # gravitational constant (m/s^2)
    m = 0.057  # projectile mass (kg)
    rho = 1.23  # air density (kg/m^3)
    D = 0.065  # projectile diameter (m)
    s = (np.pi/4) * D**2
    c_d = 0.45  # coefficient of drag for a sphere
    C = (rho * s * c_d) / (2 * m)

    return [vx,
            -C*vx*np.sqrt(vx**2 + vy**2),
            vy,
            -C*vy*np.sqrt(vx**2 + vy**2) - g]


# Define the initial conditions
theta_0 = np.pi/4  # 45 degrees
V_0 = 50  # velocity at t=0 (m/s)
x_0 = 0
x_dot = V_0*np.cos(theta_0)
y_0 = 0
y_dot = V_0*np.sin(theta_0)

# Time to hit the ground
# t_f = (2 * V_0 * np.sin(theta_0)) / 9.81

# Group all the initial conditions into a vector
S_0 = (x_0, x_dot, y_0, y_dot)

# Define the time range
t = np.linspace(0, 4.8, 1000)

# Solve the coupled ODE's
# Indexes [0] and [2] are the x and y positions, respectively.
# Indexes [1] and [3] are the velocities in the x and y direction, respectively.
sol = odeint(dSdt, y0=S_0, t=t, tfirst=True)

# Extract the solutions for x1 and x2
x_sol = sol.T[0]
y_sol = sol.T[2]

# Plot x and y
plt.plot(x_sol, y_sol, label=f"Launch angle: {theta_0*180/np.pi}°\nInitial Velocity: {V_0} m/s")
plt.title("Projectile with air friction")
plt.ylabel(r"$y\; (m)$")
plt.xlabel(r"$x\; (m)$")
plt.ylim(top=30)
plt.ylim(bottom=0)
plt.legend()
plt.gca().set_aspect('equal', 'box')
plt.show()
