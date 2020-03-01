#!/usr/bin/env python2

import rospy
from h264_image_transport.msg import H264Packet
from tello_driver.msg import test
import av
import cv2
import numpy as np
import threading
import traceback
import time


class StandaloneVideoStream(object):
    def __init__(self):
        self.cond = threading.Condition()
        self.queue = []
        self.closed = False

    def read(self, size):
        self.cond.acquire()
        try:
            if len(self.queue) == 0 and not self.closed:
                self.cond.wait(2.0)
            data = bytes()
            while 0 < len(self.queue) and len(data) + len(self.queue[0]) < size:
                data = data + self.queue[0]
                del self.queue[0]
        finally:
            self.cond.release()
        return data

    def seek(self, offset, whence):
        return -1

    def close(self):
        self.cond.acquire()
        self.queue = []
        self.closed = True
        self.cond.notifyAll()
        self.cond.release()

    def add_frame(self, buf):
        self.cond.acquire()
        self.queue.append(buf)
        self.cond.notifyAll()
        self.cond.release()


stream = StandaloneVideoStream()


def callback(msg):
  #rospy.loginfo('frame: %d bytes' % len(msg.data))
  #if len(msg.data) > 1000:  
    stream.add_frame(msg.data)

def findGreenMask(img):
  low_green_0 = np.array([35,150,0])
  upper_green_0 = np.array([80,255,255])
  rm = cv2.inRange(img, low_green_0, upper_green_0)
  return rm
def findRedMask(img):
  low_red_0 = np.array([0,150,0])
  upper_red_0 = np.array([7,255,255])
  low_red_1 = np.array([173,150,0])
  upper_red_1 = np.array([180,255,255])
  rm0 = cv2.inRange(img, low_red_0, upper_red_0)
  rm1 = cv2.inRange(img, low_red_1, upper_red_1)
  rm = cv2.bitwise_or(rm0, rm1)
  return rm
def findYellowMask(img):
  low_yellow_0 = np.array([25,150,0])
  upper_yellow_0 = np.array([35,255,255])
  rm = cv2.inRange(img, low_yellow_0, upper_yellow_0)
  return rm

def main():

    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    out = cv2.VideoWriter('test_contour.avi', fourcc, 30.0, (1920, 720))
    rospy.init_node('h264_listener')
    rospy.Subscriber("/tello/image_raw/h264", H264Packet, callback)
    pub = rospy.Publisher('/selfDefined', test, queue_size = 1)
    container = av.open(stream)
    rospy.loginfo('main: opened')
    frame_skip = 300
    for frame in container.decode(video=0):
        if 0 < frame_skip:
          frame_skip -= 1
          continue
        start_time = time.time()
        image = cv2.cvtColor(np.array(frame.to_image()), cv2.COLOR_RGB2BGR)
        blurred_img = cv2.GaussianBlur(image, (13, 13), 0)
        hsv_img = cv2.cvtColor(blurred_img.copy(), cv2.COLOR_BGR2HSV)

        # find red mask
        red_mask = findRedMask(hsv_img)   
        (c_i_red, c_c_red, c_h_red) = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # find green mask
        green_mask = findGreenMask(hsv_img)   
        (c_i_green, c_c_green, c_h_green) = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # find yellow mask
        yellow_mask = findYellowMask(hsv_img)   
        (c_i_yellow, c_c_yellow, c_h_yellow) = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(c_c_green) == 0 :
            green_area = 0
        else :
            # find max contour of green
            green_max = max(c_c_green, key = cv2.contourArea)
            x_green,y_green,w_green,h_green = cv2.boundingRect(green_max)
            green_area = w_green * h_green
            if green_area < 100 :
                green_area = 0

        if len(c_c_red) == 0 :
            red_area = 0
        else :
            # find max contour of red
            red_max = max(c_c_red, key = cv2.contourArea)
            x_red,y_red,w_red,h_red = cv2.boundingRect(red_max)
            red_area = w_red * h_red
            if red_area < 100:
                red_area = 0
        if len(c_c_yellow) == 0:
            yellow_area = 0
        else :
            # find max contour of yellow
            yellow_max = max(c_c_yellow, key = cv2.contourArea)
            x_yellow,y_yellow,w_yellow,h_yellow = cv2.boundingRect(yellow_max)
            yellow_area = w_yellow * h_yellow
            if yellow_area < 100 :
                yellow_area = 0

        # determine different status and publish message
        if red_area > green_area > yellow_area and red_area > 200:

            show_image = cv2.cvtColor(c_i_red, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(show_image,(x_red,y_red),(x_red+w_red,y_red+h_red),(0,255,0),2)
            m = test()
            m.l1 = [x_red,y_red]
            m.l2 = "red"
            pub.publish(m)
            out.write(np.concatenate((blurred_img, show_image), axis=1))
            cv2.imshow('result', np.concatenate((blurred_img, show_image), axis=1))
            cv2.waitKey(1)

        elif green_area > yellow_area > red_area and green_area > 200 :

            show_image = cv2.cvtColor(c_i_green, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(show_image,(x_green,y_green),(x_green+w_green,y_green+h_green),(0,255,0),2)
            m = test()
            m.l1 = [x_red,y_red]
            m.l2 = "green"
            pub.publish(m)
            out.write(np.concatenate((blurred_img, show_image), axis=1))
            cv2.imshow('result', np.concatenate((blurred_img, show_image), axis=1))
            cv2.waitKey(1)

        elif yellow_area > red_area > green_area and yellow_area > 200 :

            show_image = cv2.cvtColor(c_i_yellow, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(show_image,(x_yellow,y_yellow),(x_yellow+w_yellow,y_yellow+h_yellow),(0,255,0),2)
            m = test()
            m.l1 = [x_red,y_red]
            m.l2 = "yellow"
            pub.publish(m)
            out.write(np.concatenate((blurred_img, show_image), axis=1))
            cv2.imshow('result', np.concatenate((blurred_img, show_image), axis=1))
            cv2.waitKey(1)

        else :
            m = test()
            m.l1 = [0,0]
            m.l2 = "stay"
            pub.publish(m)
            out.write((blurred_img))
            cv2.imshow('result', blurred_img)
            # cv2.waitKey(1)

        if frame.time_base < 1.0/60:
          time_base = 1.0/60
        else:
          time_base = frame.time_base
        frame_skip = int((time.time() - start_time)/time_base)

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        traceback.print_exc()
    finally:
        stream.close()
        cv2.destroyAllWindows()
