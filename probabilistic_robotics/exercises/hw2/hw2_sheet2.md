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
>\left(\begin{array}{cc} 
>l_xcos(\theta_1)-l_ysin(\theta_1)+x_1 \\ 
>l_xsin(\theta_1)+l_ycos(\theta_1)+y_1 \\
> \theta_1 
>\end{array}\right) \\
>$$

> solution : 
> $$
> t_{Gl} = T_{G1}t_{1l} + t_{G1} 
> \\=
>\left(\begin{array}{cc} 
>R(\theta_1) & t_1\\
>0 & 1
>\end{array}\right)
>\left(\begin{array}{cc} 
> t_{1l} \\ 
>0 
>\end{array}\right) +
>\left(\begin{array}{cc} 
> t_{G1} \\ 
>0 
>\end{array}\right) \\
>=
>\left(\begin{array}{cc} 
>cos(\theta_1) & -sin(\theta_1) & x_1 \\
>sin(\theta_1) & cos(\theta_1) & y_1 \\
>0 & 0 & 1
>\end{array}\right)
>\left(\begin{array}{cc} 
>l_x \\ l_y \\ 0
>\end{array}\right)
>+
>\left(\begin{array}{cc} 
>x_1 \\ y_1 \\ \theta_1
>\end{array}\right) \\
>=
>\left(\begin{array}{cc} 
>l_xcos(\theta_1)-l_ysin(\theta_1)+x_1 \\ 
>l_xsin(\theta_1)+l_ycos(\theta_1)+y_1 \\
> \theta_1 
>\end{array}\right) \\
>
>$$

#### (b)
> The coordinates of the landmark in robot's local frame is:
> $$t_{1l}$$
> where
> $$t_{1l} = T_{1G}t_{Gl} + t_{1G}$$
> In the equation above, $T_{1G}$ is the inverse of $T_{G1}$, which is know ; $t_{Gl}$ is given by the question ; $t_{1G}$ can also be calculate easily from $t_{G1}$ .
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
> The coordinate of landmark $l$ w.r.t the robot's local frame now is :
> $$
> t_{2l} = T_{21}t_{1l} + t_{21} 
> = T_{12}^{-1}t_{1l} + t_{21} 
> \\=
>\left(\begin{array}{cc} 
>R(\theta_2 - \theta_1)^T & -R(\theta_2-\theta_1)^TR\theta_1^T(t_2-t_1) \\
>0 & 1
>\end{array}\right)
>\left(\begin{array}{cc} 
> t_{1l} \\ 
>0 
>\end{array}\right) +
>\left(\begin{array}{cc} 
> t_{21} \\ 
>0 
>\end{array}\right) \\
>=
>\left(\begin{array}{cc} 
>R(\theta_1 - \theta_2) & R(\theta_2)^T(t_1-t_2) \\
>0 & 1
>\end{array}\right)
>\left(\begin{array}{cc} 
> t_{1l} \\ 
>0 
>\end{array}\right) +
>\left(\begin{array}{cc} 
> t_{21} \\ 
>0 
>\end{array}\right) \\
>$$
<br/>

### Exercise 3: Sensing
---

#### (a)
> python file is `hw2_sensing.py`
> 
> ![alt text](/hw2/hw2_sensing.png "hw2_sensing_a")

#### (b)
> According to the graph shown, the robot(sesor) should be in a corridor which has "transparent walls" like big windows or something. Most of the scans reflected on the "transparent walls",hence the two parellel lines; and some went straight through and reflected on the further walls and objects. 

#### (c)
> python file is `hw2_sensing.py`
> 
> ![alt text](/hw2/hw2_sensing_ground.png "hw2_sensing_ground")