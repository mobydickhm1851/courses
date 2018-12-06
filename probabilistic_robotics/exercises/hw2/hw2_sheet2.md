# HW Sheet 2 : Linear Algebra

### Exercise 1 : Linear Alegbra 
---

#### (a) 
> No, using $[Z_1, Z_2]$ $A$ $[Z_1, Z_2]^T$ to verify.

#### (b) 
> Largets value is $\mu = -1$ 
#### (c)
> See `hw2_orthognality.py`
#### (d)
> Yes, it's orthogonal. 
>
> Because the multiplication (dot) of D and D^T is an __identity matrix__.

<br/>

### Exercise 2: 2D Transformations as Affine Matrices
---

#### (a)
> The coordinates of $l$ $w.r.t.$ the global frame is :
> $$
>t_{Gl} = 
>\left(\begin{array}{cc} 
>l_xcos\theta_1 - l_ysin\theta_1 + x_1 \\
>l_xsin\theta_1 + l_ycos\theta_1 + y_1 
>\end{array}\right)
>$$

> solution : 
> $$
> T_{Gl} = T_{G1}T_{1l} =
>\left(\begin{array}{cc} 
>R(\theta_1) & t_1\\
>0 & 1
>\end{array}\right)
>\left(\begin{array}{cc} 
>R(0) & t_l \\ 
>0 & 1
>\end{array}\right)\\ 
>
>=
>\left(\begin{array}{cc} 
>R(\theta_1)R(0) & R(\theta_1)t_l+t_1 \\
>0 & 1
>\end{array}\right)
>=
>\left(\begin{array}{cc} 
>R(\theta_1) & t_{Gl} \\
>0 & 1
>\end{array}\right)\\
>t_{Gl} = 
>\left(\begin{array}{cc} 
>l_xcos\theta_1 - l_ysin\theta_1 + x_1 \\
>l_xsin\theta_1 + l_ycos\theta_1 + y_1 
>\end{array}\right)
>$$

#### (b)
> use $T_{Gl}^{-1}$

#### (c)
> $$
> T_{12} = T_{1G}T_{G2} = T_{G1}^{-1}T_{G2} \\
> = \left(\begin{array}{cc} 
> R(\theta_1)^T & -R(\theta_1)^Tt_1 \\
> 0  &  1  
> \end{array}\right)
> \left(\begin{array}{cc} 
> R(\theta_2) & t_2 \\
> 0  &  1 
> \end{array}\right) \\
> = \left(\begin{array}{cc} 
> R(\theta_1)^TR(\theta_2) & R(\theta_1)^Tt_2-R(\theta_1)^Tt_1 \\
> 0  &  1 
> \end{array}\right) \\
> = \left(\begin{array}{cc} \\
> R(\theta_2-\theta_1) & R(\theta_1)^T(t_2-t_1) \\
> 0  &  1 \\
> \\
> \end{array}\right)
> $$


#### (d)
> $$
> T_{2l} = T_{21}T_{1l} = T_{2G}T_{Gl} = T_{G2}^{-1}T_{Gl} \\
> = \left(\begin{array}{cc} 
> R(\theta_2)^T & -R(\theta_2)^Tt_2 \\
> 0  &  1 
> \end{array}\right)
> \left(\begin{array}{cc} 
> R(\theta_1) & t_{Gl} \\
> 0  &  1 
> \end{array}\right) \\
> = \left(\begin{array}{cc} \\
> R(\theta_1-\theta_2) & R(\theta_2)^T(t_{Gl}-t_2) \\
> 0  &  1 \\
> \\
> \end{array}\right)
> $$

<br/>

### Exercise 3: Sensing
---

#### (a)
> ![alt text](/hw2/hw2_sensing.png "hw2_sensing_a")

#### (b)
> According to the graph shown, the robot(sesor) should be in a corridor which has "transparent walls" like big windows or something. Most of the scans reflected on the "transparent walls",hence the two parellel lines; and some went straight through and reflected on the further walls and objects. 

#### (c)
    