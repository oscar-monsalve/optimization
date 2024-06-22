# Optimization: single-variable problems

single-variable exercises from the book "Optimization Fundamentals (2018, Springer)".

## The lifeguard problem

Find a path to the swimmer that minimizes time, see Figure 1. The objective function is time, and the
design variable is x, the point at which the lifeguard enters the water.

The objective function must be written as a function of the design variable. First, the total time is the sum of
the times that take the lifeguard to go over the sand and water:

$t = t_s + t_w = \frac{L_s}{v_s} + \frac{L_w}{v_w}$

where $t$ is the total time, and $t_s,\\,t_w$ are the times over the sand and water, respectively. $L_s,\\, L_w$ are
the straight line lengths over the sand and water, respectively. $v_s,\\, v_w$ are the velocities of the lifeguard
over the sand and water, respectively.

<figure>
    <img src="images/1.lifeguard.png" alt="The lifeguard problem" width="400" height="auto"/>
    <figcaption>Figure 1. The lifeguard problem.</figcaption>
</figure>
