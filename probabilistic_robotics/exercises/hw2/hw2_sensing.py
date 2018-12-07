#!/usr/bin/env python3

from math import pi as pi
import numpy as np
import matplotlib.pyplot as plt


scan = np.loadtxt("./hw2/laserscan.dat")

# From Polar coordinate to Cartesian coordinate
def give_coordinate(scan_ls, scan_range):
    # set angle to scan point in scan_ls
    angle = np.linspace(-scan_range/2, scan_range/2, np.shape(scan_ls)[0], endpoint = True)
    xy_cor = np.array([[0,0]])
    # x_cor, y_cor = [], []     # list for x-y coordinate
    for i in range(len(scan_ls)):
        x_cor = scan_ls[i]*np.cos(angle[i])
        y_cor = scan_ls[i]*np.sin(angle[i])
        if i == 0:
            xy_cor[i,i] = x_cor
            xy_cor[i,i+1] = y_cor
        else:
            xy_cor = np.append(xy_cor, np.array([[x_cor, y_cor]]), 0)

    return xy_cor

# Orientation of subject
def R(th):
    R_arr = np.array([[np.cos(th), -np.sin(th)],
                       [np.sin(th), np.cos(th)]])
    return R_arr

# Homogeneous Transformation matrices 
def HTM(R, t):
    HTM_arr = np.append(np.append(R, t.T, 1), [[0, 0, 1]], 0)
    return HTM_arr

# from ground to robot (gr)
T_gr = HTM(R(pi/4), np.array([[1,0.5]]))
# from robot to sensor (rs)
T_rs = HTM(R(pi), np.array([[0.2,0.0]]))
# from ground to sensor (gs)
T_gs = T_gr @ T_rs

# get landmark(scan) coordinate from ground
# note: t_sl[i].shape = (2,); t_gs.shape = (3,)
def get_cor_lm(T_gs, t_sl, t_gs):
    for i in range(t_sl.shape[0]):
        t_sl_mod = np.append(t_sl[i],[1], 0)
        t_gl = T_gs @ t_sl_mod.T 
        if i == 0:
            cor_lm = np.array([t_gl])
        else:
            cor_lm = np.append(cor_lm, [t_gl], 0)

    return cor_lm

# print(get_cor_lm(T_gs, cor_scan, np.array([1,0.5,pi/4])))

# The following plt is in sensor's coordiante
robot_pose = np.array([1,0.5,pi/4])
cor_scan = give_coordinate(scan, pi)
plt_x_sensor, plt_y_sensor, plt_x_ground, plt_y_ground = [], [], [], []
[plt_x_sensor.append(cor_scan[i,0]) for i in range(cor_scan.shape[0])]
[plt_y_sensor.append(cor_scan[i,1]) for i in range(cor_scan.shape[0])]
cor_scan_ground = get_cor_lm(T_gs, cor_scan, robot_pose)
[plt_x_ground.append(cor_scan_ground[i,0]) for i in range(cor_scan_ground.shape[0])]
[plt_y_ground.append(cor_scan_ground[i,1]) for i in range(cor_scan_ground.shape[0])]

fig, ax = plt.subplots()
# scan coordinate from sensor
#ax.scatter(plt_x_sensor, plt_y_sensor, c = 'red', s = 50, label = 'scan_sensor',alpha = 0.3, edgecolors = 'none')
# scan coordinate from ground
ax.scatter(plt_x_ground, plt_y_ground, c = 'green', s = 5, label = 'scan_ground',alpha = 0.7, edgecolors = 'none')
# robot coordinate from ground
ax.scatter(robot_pose[0], robot_pose[1], c = 'blue', s = 100, label = 'ROBOT', alpha = 0.5)
ax.legend()
ax.grid(True)

plt.show()

# The following plt is in world's coordinate
