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

# Find the optimal angle for the initial velocity and the constant C
# Define constants
g = 9.81  # gravitational constant (m/s^2)
m = 0.057  # projectile mass (kg)
rho = 1.23  # air density (kg/m^3)
D = 0.065  # projectile diameter (m)
s = (np.pi/4) * D**2
c_d = 0.45  # coefficient of drag for a sphere
C = (rho * s * c_d) / (2 * m)

# The following function calcultes the x coordinate at which the projectile reaches the ground:


def get_distance(angle: float, v: float, t=10) -> float:
    vx_0 = v*np.cos(np.deg2rad(angle))
    vy_0 = v*np.sin(np.deg2rad(angle))
    sol = odeint(dSdt, y0=(0, vx_0, 0, vy_0), t=np.linspace(0, t, 10000), tfirst=True)
    just_above_idx = np.where(np.diff(np.sign(sol.T[2])) < 0)[0][0]
    just_below_idx = just_above_idx + 1
    x_loc = (sol.T[0][just_above_idx] + sol.T[0][just_below_idx]) / 2
    return x_loc


# Show how the travelled distance changes as a function of the launch angle and initial velocity:
# print(f"Travelled distance at 60° launch angle: {get_distance(60, V_0)}")
# print(f"Travelled distance at 50° launch angle: {get_distance(50, V_0)}")
# print(f"Travelled distance at 45° launch angle: {get_distance(45, V_0)}")
# print(f"Travelled distance at 40° launch angle: {get_distance(40, V_0)}")
# print(f"Travelled distance at 35° launch angle: {get_distance(35, V_0)}")
# print(f"Travelled distance at 30° launch angle: {get_distance(30, V_0)}")

# Now, we evaluate various launch angles within a range to find the maximum travlled distance:
angles = np.linspace(25, 60, 300)
x_locs = np.vectorize(get_distance)(angles, V_0)

# Plot the travelled distance as a function of the launch angle and V_0 = 50 m/s
max_index = np.argmax(x_locs)
optimum_angle = angles[max_index]
max_y = x_locs[max_index]

plt.plot(angles, x_locs)
plt.scatter(optimum_angle, max_y, color='red', zorder=5)  # Adding the point
plt.annotate(f"Max. range: {max_y:.2f} m\nat angle: {optimum_angle:.2f}°", xy=(optimum_angle, max_y),
             xytext=(optimum_angle-3, max_y-4),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10)
plt.xlabel(r"Launch angles $\theta_0$ (°)")
plt.ylabel("Range (m)")
plt.title(r"Launch angles vs. travelled distance (range) for $V_0 = 50\; m/s$")
plt.xlim(left=25, right=60)
plt.grid(True)
plt.show()

# Plot x and y
# plt.plot(x_sol, y_sol, label=f"Launch angle: {theta_0*180/np.pi}°\nInitial Velocity: {V_0} m/s")
# plt.title("Projectile with air friction")
# plt.ylabel(r"$y\; (m)$")
# plt.xlabel(r"$x\; (m)$")
# plt.ylim(top=30)
# plt.ylim(bottom=0)
# plt.legend()
# plt.gca().set_aspect('equal', 'box')
# plt.tight_layout()
# plt.show()
