#!/usr/bin/python
import rospy
from geometry_msgs.msg import Twist

def callback(data):
    print(data.linear)
    print('===================')
    print(data.angular)
    print('===================')

def turtle_sub():
    print('test1')
    rospy.init_node('turtlesim_sub', anonymous=True)
    print('test2')
    rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)
    print('test3')    
    
    # spin simply keeps python from exiting until this node is stop
    rospy.spin()
    print('test4')    
    
   

if __name__ == '__main__':
    turtle_sub()
