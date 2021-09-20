#!/usr/bin/env python3
# license removed for brevity

import roslib; roslib.load_manifest('paquete0')
import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Point, Pose

import numpy as np 
import math

def talker():
    pub = rospy.Publisher('posicion1', Pose, queue_size=10)
    rospy.init_node('lab3p2', anonymous=True) #nombre del nodo
    rate = rospy.Rate(1) # 10hz
    poseEfector = Pose()

    l1 = 0.3
    l2 = 0.2
    q1 = 0
    q2 = 0
    Rq1 = ([math.cos(q1), -math.sin(q1),0],
            [math.sin(q1), math.cos(q1),0],
            [0,0,1])
    Tl1 = ([1,0,l1],
            [0,1,0],
            [0,0,1])
    Tl2 = ([1,0,l2],
            [0,1,0],
            [0,0,1])
    p0 = np.array([0,0,1]).transpose()

    while q2<=1.6:
        Rq2 = ([math.cos(q2),-math.sin(q1),0],
                [math.sin(q2), math.cos(q2),0],
                [0,0,1])
        p= np.matmul(np.matmul(np.matmul(np.matmul(Rq1,Tl1),Rq2),Tl2),p0)
        poseEfector.position.x = p[0]
        poseEfector.position.y = p[1]
        poseEfector.position.z = 0
        pub.publish(poseEfector)
        q2 = q2+0.1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
