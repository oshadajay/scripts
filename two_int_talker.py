#!/usr/bin/env python  
import random

import rospy
from std_msgs.msg import Int16
from activity_1.msg import TwoInts

def talker():
    pub = rospy.Publisher('/two_ints', TwoInts, queue_size=10)
    rospy.init_node('two_int_talker_node', anonymous=True)
    rate = rospy.Rate(0.5)  
    random.seed()

    while not rospy.is_shutdown():

        msg = TwoInts()
  
        msg.a = random.randint(1,20)
        msg.b = random.randint(1,20)
        rospy.loginfo("{} and {} are published".format( msg.a,msg.b))
        pub.publish(msg)
        rate.sleep()
    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



        