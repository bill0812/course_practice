#!/usr/bin/python
import rospy
from geometry_msgs.msg import Twist

def turtle_pub():
    # The queue_size argument is new in ROS hydro 
    # and limits the amount of queued messages if any
    # subscriber is not receiving then fast enough
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)
    rospy.init_node('turtlesim_pub',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown() :
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = -1.8
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__' :
    try :
        turtle_pub()
    except rospy.ROSInterruptException:
        pass
