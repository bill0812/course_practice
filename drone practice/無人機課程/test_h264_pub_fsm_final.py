#!/usr/bin/env python
import rospy
import roslib
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty, UInt8
from tello_driver.msg import TelloStatus, test
from statemachine import StateMachine, State
from time import sleep


global canLand
canLand = False

global cantakeoff
cantakeoff = False

def ts_callback(data):
  global canLand
  if data.fly_mode == 12:
    canLand = True 

class sMachine(StateMachine):
	stay = State('stay', initial = True)
	red = State('red')
	yellow = State('yellow')
	green = State('green')
	# red light and green light
	to_stay = yellow.to(stay) | stay.to(stay) | green.to(stay)
	to_green = stay.to(green) | green.to(green) | red.to(green) | yellow.to(green)
	to_yello = green.to(yellow) | yellow.to(yellow) | stay.to(yellow)
	to_red = yellow.to(red) | stay.to(red) | red.to(red)
	
	# original code of TA
	# to_hover = hover.to(hover) | addSp.to(hover) | correction.to(hover) | forward.to(hover)
	# to_correction = hover.to(correction) | correction.to(correction) | forward.to(correction)
	# to_forward = hover.to(forward) | correction.to(forward) | forward.to(forward)
	# to_addSp = forward.to(addSp) | correction.to(addSp)

class MyModel(object):
	def __init__(self, state):
		self.state = state
		self.target = (-1,-1,1)
		self.center = (480, 320)
		self.check = False
		self.canLand = False
		self.cantakeoff = False
		self.rec_time = 0
		self.self_pub = rospy.Subscriber('/selfDefined', test, self.cback)
		self.cmd_pub = rospy.Publisher('/tello/cmd_vel', Twist, queue_size = 10)
		self.takeoff_pub = rospy.Publisher('/tello/takeoff', Empty, queue_size = 1)
		self.rate = rospy.Rate(10)
		self.light = "stay"
	

	def cback(self, data):
		self.rec_time = rospy.get_time()
		self.target = data.l1
		self.light = data.l2

	def run(self, fsm):
		#print(type(self))
		while not rospy.is_shutdown():
			msg = Twist()
			print(self.state)
			if fsm.is_green:
				if self.target[0] - self.center[0] != 0:
					msg.linear.y = -(self.target[0] - self.center[0]) / abs((self.target[0] - self.center[0])) * 0.1
				if self.target[1] - self.center[1] != 0:
					msg.linear.z = -(self.target[1] - self.center[1]) / abs((self.target[1] - self.center[1])) * 0.2
				msg.linear.x = 0.25
				self.cmd_pub.publish(msg)
				self.rate.sleep()
				if self.light == "red" :
					fsm.to_red()
				elif self.light == "yellow" :
					fsm.to_yello()
				elif self.light == "green" :
					fsm.to_green()
				else :
					fsm.to_stay()
			elif fsm.is_yellow:
				if self.target[0] - self.center[0] != 0:
					msg.linear.y = -(self.target[0] - self.center[0]) / abs((self.target[0] - self.center[0])) * 0.1
				if self.target[1] - self.center[1] != 0:
					msg.linear.z = -(self.target[1] - self.center[1]) / abs((self.target[1] - self.center[1])) * 0.2
				msg.linear.x = 0.1
				self.cmd_pub.publish(msg)
				self.rate.sleep()
				if self.light == "red" :
					fsm.to_red()
				elif self.light == "yellow" :
					fsm.to_yello()
				elif self.light == "green" :
					fsm.to_green()
				else :
					fsm.to_stay()
			elif fsm.is_red:
				if self.target[0] - self.center[0] != 0:
					msg.linear.y = -(self.target[0] - self.center[0]) / abs((self.target[0] - self.center[0])) * 0.1
				if self.target[1] - self.center[1] != 0:
					msg.linear.z = -(self.target[1] - self.center[1]) / abs((self.target[1] - self.center[1])) * 0.2
				msg.linear.x = 0
				self.cmd_pub.publish(msg)
				self.rate.sleep()
				sleep(2.5)
				L()
				if self.light == "red" :
					fsm.to_red()
				elif self.light == "yellow" :
					fsm.to_yello()
				elif self.light == "green" :
					fsm.to_green()
				else :
					fsm.to_stay() 
			elif fsm.is_stay:
				msg.linear.x = 0
				self.cmd_pub.publish(msg)
				self.rate.sleep()
				sleep(2.5)
				if self.light == "red" :
					fsm.to_red()
				elif self.light == "yellow" :
					fsm.to_yello()
				elif self.light == "green" :
					fsm.to_green()
				else :
					fsm.to_stay()

def L():
  global canLand
  land_sub = rospy.Subscriber('/tello/status', TelloStatus, ts_callback)
  land_pub = rospy.Publisher('/tello/land', Empty, queue_size = 1)
  rate = rospy.Rate(10)
  
  while canLand is not True:
    msg = Empty()
    land_pub.publish(msg)
    rate.sleep()
    
if __name__ == '__main__':
	rospy.init_node('h264_pub', anonymous=True)
	takeoff_sub = rospy.Subscriber('/tello/status', TelloStatus)
	takeoff_pub = rospy.Publisher('/tello/takeoff', Empty, queue_size = 1)
	while takeoff_pub.get_num_connections() == 0:
		pass
	rate = rospy.Rate(10)
	msg = Empty()
	takeoff_pub.publish(msg)
	rate.sleep()
	sleep(3)
	obj = MyModel(state='stay')
	fsm = sMachine(obj)
	obj.run(fsm)

