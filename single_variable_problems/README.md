# Optimization: single-variable problems

single-variable exercises from the book "Optimization Fundamentals (2018, Springer)".

## 1. The lifeguard problem

Find a path to the swimmer that minimizes time, see Figure 1. The objective function is time, and the
design variable is x, the point at which the lifeguard enters the water.

<figure>
    <img src="images/01_lifeguard_problem.png" alt="The lifeguard problem" width="400" height="auto"/>
    <figcaption>Figure 1. The lifeguard problem.</figcaption>
    <br>
</figure>

<br>

The objective function must be written as a function of the design variable. First, the total time is the sum of
the times that take the lifeguard to go over the sand and water:

$$t = t_s + t_w = \displaystyle \frac{L_s}{v_s} + \displaystyle \frac{L_w}{v_w}$$

where $t$ is the total time, and $t_s,\\,t_w$ are the times over the sand and water, respectively. $L_s,\\, L_w$ are
the straight line lengths over the sand and water, respectively. $v_s,\\, v_w$ are the velocities of the lifeguard
over the sand and water, respectively.

Then, using the Pythogorean theorem, we can find the straight line lengths. Then, the objective function is:

$$t(x) = \displaystyle \frac{1}{7}\sqrt{50^2+x^2} + \displaystyle \frac{1}{2}\sqrt{50^2+(100-x)^2}$$

The optimum solution, meaning the minimum time, can be easily found looking for the plot's minimum coordinates.

<figure>
    <img src="images/01_lifeguard_time_function.png" alt="Time as a function of x" width="400" height="auto"/>
    <figcaption>Figure 2. Time as a function of x.</figcaption>
    <br>
</figure>

<br>

# 2. Maximum Range of a Projectile with Aerodynamics

Let’s consider a tennis ball with a diameter of 65 mm and a mass of 57 g .Since the ball can move in both
horizontally and vertically, we will need to model its motion in two directions. We’ll assume there is no spin, so
the aerodynamic drag force just acts opposite to the direction of motion. Figure 2 shows the ball with the components
of the aerodynamic drag.

<figure>
    <img src="images/02_ball_projectile_drag_components.png" alt="Figure 2. Drag components" width="400" height="auto"/>
    <figcaption>Figure 2. Drag components.</figcaption>
    <br>
</figure>

<br>

The aerodynamic drag is defined as:

$$D = \displaystyle \frac{1}{2}C_d\rho V^2 s$$

where $C_d$ is the coefficient of drag, which for a sphere is $C_d = 0.45$. $\rho$ is the air density,
$\rho = 1.23\\; kg/m^3$ at sea level. $V$ is velocity and $s$ is the cross-sectional area of the ball, $s = 0.010425\\; m^2$.

Drag can be broken down into the $x$ and $y$ directions, so we can write Newton’s law in both directions.

$D_x = D\cos(\theta)$ and $D_y = D\sin(\theta)$

$x$ direction $\sum F_x = ma_x$ $\rightarrow$ $-D_x = ma_x = m\ddot{x}$

$y$ direction $\sum F_y = ma_y$ $\rightarrow$ $-D_y - mg = ma_y = m\ddot{y}$

So the system of equations to be solved is:

$$m\ddot{x} = -\displaystyle \frac{1}{2}C_d \rho V^2 s \cos(\theta)$$

$$m\ddot{y} = -\displaystyle \frac{1}{2}C_d \rho V^2 s \sin(\theta) - mg$$

We don’t want $\theta$ to appear in the equations, so we will define $\theta$ in terms of velocity as shown in Figure 3.

<figure>
    <img src="images/02_ball_projectile_vel_components.png" alt="Figure 3. Velocity components" width="400" height="auto"/>
    <figcaption>Figure 3. Velocity components.</figcaption>
    <br>
</figure>

<br>

Then, we can use the following relationships to put the two differential equations in their final form.

$V = \sqrt{V_x^2 + V_y^2}$ and $V^2 = V_x^2 + V_y^2$

$\cos(\theta) = \displaystyle \frac{V_x}{V} = \displaystyle \frac{V_x}{\sqrt{V_x^2 + V_y^2}}$ and $\sin(\theta) = \displaystyle \frac{V_y}{V} = \displaystyle \frac{V_y}{\sqrt{V_x^2 + V_y^2}}$

Substituting these into the previous two equations gives:

$$\ddot{x} = -C V_x \sqrt{V_x^2 + V_y^2}$$

$$\ddot{y} = -C V_y \sqrt{V_x^2 + V_y^2} - g$$

where

$C = \displaystyle \frac{1}{2m}\rho s C_d$ is a constant containing all physical considerations.

Before we can solve these equations, we need some initial conditions. If we write the equations in terms of position,
there are two second-order equations, so we will need four initial conditions:

- Let’s assume the ball starts at the origin, so $x(0) = 0$ and $y(0) = 0$.
- Let’s also assume that the initial velocity is $V_0 = 50\\; m/s$.
- The launch angle is $\theta_0 = 45^{\circ}$.

The intial conditions are:

- $x(0) = 0$
- $y(0) = 0$
- $\dot{x}(0) = V_0\cos(\theta_0)$
- $\dot{y}(0) = V_0\sin(\theta_0)$

To solve numerically in Python the two-coupled second order linear ODE's, we need to reduce the order of each
differential equation. To do so, we make use of the state-space representation introducing two new variables $v_x$
and $v_y$. Then, we define them as $v_x = \dot{x}$ and $v_y = \dot{y}$. With this, we can construct 4-coupled first-
order linear ODE's:

- $\dot{x} = v_x$
- $\dot{v}_x = \ddot{x} = -Cv_x \sqrt{v_x^2 + v_y^2}$
- $\dot{y} = v_y$
- $\dot{v}_y = \ddot{y} = -Cv_y \sqrt{v_x^2 + v_y^2} - g$

Now, we have six coupled first order ODE's. We want to solve for $\dot{x},\\; v_x,\\; \dot{y},\\; v_y$. Rewriting
them in vector form we have the following:

$$
\vec{S} = \begin{bmatrix}
x \\
v_x \\
y \\
v_y
\end{bmatrix} \Longrightarrow
\displaystyle \frac{d\vec{S}}{dt} = \begin{bmatrix}
\dot{x} \\
\dot{v}_x \\
\dot{y} \\
\dot{v}_y
\end{bmatrix} = \begin{bmatrix}
v_x \\
-Cv_x\sqrt{v_x^2 + v_y^2} \\
v_y \\
-Cv_y\sqrt{v_x^2 + v_y^2} - g
\end{bmatrix}
$$
