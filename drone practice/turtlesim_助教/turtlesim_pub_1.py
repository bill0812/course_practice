#!/usr/bin/env python2
import rospy
import roslib
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from time import sleep

global cont
cont = True

def callback(data):
  global cont
  if data:
    cont = False

def TO():
  takeoff_pub = rospy.Publisher('/tello/takeoff', Empty, queue_size = 1)
  rospy.init_node('turtlesim_pub', anonymous=True)
  rate = rospy.Rate(10)
  msg = Empty()
  rospy.loginfo(msg)
  takeoff_pub.publish(msg)
  rate.sleep()

def cmd():
  #The queue_size argument is New in ROS hydro and limits the amount of queued messages if any subscriber is not receiving them fast enough
  
  cmd_pub = rospy.Publisher('/tello/cmd_vel', Twist, queue_size = 10)
  rate = rospy.Rate(10)
  count = 10
  while not rospy.is_shutdown():
    if count > 0:
      msg = Twist()
      msg.linear.x = 0.4
      msg.angular.z = 0.36
      rospy.loginfo(msg)
      cmd_pub.publish(msg)
      rate.sleep()
      count -= 1
    else:
      #msg = Twist()
      #cmd_pub.publish(msg)
      #rate.sleep()
      break
  print("end loop")
  sleep(3)

def L():
  global cont
  land_sub = rospy.Subscriber('/tello/land', Empty, callback)
  land_pub = rospy.Publisher('/tello/land', Empty, queue_size = 1)
  rate = rospy.Rate(10)
  
  while cont == True:
    msg = Empty()
    #rospy.loginfo(msg)
    land_pub.publish(msg)
    rate.sleep()
  
if __name__ == '__main__':
  try:
    TO()
    #sleep(3)
    #cmd()
    sleep(3)
    L()
  except rospy.ROSInterruptException:
    pass
  finally:
    sys.exit(0)
