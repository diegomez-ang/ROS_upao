#!/usr/bin/env python3

import roslib; roslib.load_manifest('paquete0')
import rospy
import math
import numpy as np

# inicializa nodo ROS
rospy.init_node('lab3p1');

tx = input('tx: ')
ty = input('ty: ')
theta = input('tetha: ')
pr_x = input('pr_x: ')
pr_y = input('pr_y: ')

pr = np.array([pr_x,pr_y,1]).transpose()

R = ([math.cos(theta), -math.sin(theta), tx],
      [math.sin(theta), math.cos(theta), ty],
      [0,0,1])

prW = np.matmul(R,pr)

print(prW)
