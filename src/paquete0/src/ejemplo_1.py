#!/usr/bin/env python3
import roslib; roslib.load_manifest('paquete0')
import rospy
import math
import numpy as np #libreria numpy algebr lineal python

#inicializa nodo ros

rospy.init_node('ejemplo_1')

A = np.array([1,2,3])
B = np.array([4,5,6])
C = np.dot(A,B) #producto punto
print('el resultado es: '+ str(C))
