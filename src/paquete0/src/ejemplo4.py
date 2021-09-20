#!/usr/bin/env python3

import roslib; roslib.load_manifest('paquete0')
import rospy
import math
import numpy as np

# inicializa nodo ROS
rospy.init_node('ejemplo4');

A = np.array([1,0,1])
B = np.transpose(A)
Rz = ([math.cos(math.pi/4), -math.sin(math.pi/4), 0],
      [math.sin(math.pi/4), math.cos(math.pi/4), 0],
      [0,0,1])

T = ([1,0,1],
     [0,1,0],
     [0,0,1])

#Tr = np.matmul(Rz,T)
#p1 = np.matmul(Tr,A)
Tr = np.matmul(T,Rz)
p1 = np.matmul(Tr,A)

print(A)
print(B)
print(T)
print(Tr)
print(p1)

