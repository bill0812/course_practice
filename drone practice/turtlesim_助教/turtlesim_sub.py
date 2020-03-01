#!/usr/bin/env python2
import rospy
import roslib
import cv2
import numpy as np

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import UInt8

def callback(data):
  bridge = CvBridge()
  try: 
    img = bridge.imgmsg_to_cv2(data, "bgr8")
  except CvBridgeError as e:
    print(e)
  
  cv2.imshow('Original', img)
  cv2.imshow('Canny', cv2.Canny(img, 100, 200))
  cv2.waitKey(1)

def turtle_sub():
  rospy.init_node('turtlesim_sub', anonymous=True)
  rospy.Subscriber("/tello/image_raw", Image, callback)
  #rospy.Subscriber("/selfDefined", UInt8, secallback)
  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()

if __name__ == '__main__':
  turtle_sub()
