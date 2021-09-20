#!/usr/bin/env python3

import roslib; roslib.load_manifest('paquete0')
import rospy
import math
import numpy as np

# inicializa nodo ROS
rospy.init_node('ejemplo3_1');

A = np.array([1,0,1])
B = np.transpose(A)
Rz = ([math.cos(math.pi/2), -math.sin(math.pi/2), 0],
      [math.sin(math.pi/2), math.cos(math.pi/2), 0],
      [0,0,1])

C = np.matmul(Rz,B)

print(B)
print(Rz)
print(C)
