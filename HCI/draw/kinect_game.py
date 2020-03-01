# PyKinect
# Copyright(c) Microsoft Corporation
# All rights reserved.
# 
# Licensed under the Apache License, Version 2.0 (the License); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0
# 
# THIS CODE IS PROVIDED ON AN  *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY
# IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
# MERCHANTABLITY OR NON-INFRINGEMENT.
# 
# See the Apache Version 2.0 License for specific language governing
# permissions and limitations under the License.

import thread
import itertools
import ctypes
import cv2
import numpy

import pykinect
from pykinect import nui
from pykinect.nui import JointId

import pygame
from pygame.color import THECOLORS
from pygame.locals import *


# ===============================================================================================
# define some variables
KINECTEVENT = pygame.USEREVENT
WINSIZE = 1280,960
pygame.init()

skeleton_to_depth_image = nui.SkeletonEngine.skeleton_to_depth_image

# recipe to get address of surface: http://archives.seul.org/pygame/users/Apr-2008/msg00218.html
if hasattr(ctypes.pythonapi, 'Py_InitModule4'):
   Py_ssize_t = ctypes.c_int
elif hasattr(ctypes.pythonapi, 'Py_InitModule4_64'):
   Py_ssize_t = ctypes.c_int64
else:
   raise TypeError("Cannot determine type of Py_ssize_t")

_PyObject_AsWriteBuffer = ctypes.pythonapi.PyObject_AsWriteBuffer
_PyObject_AsWriteBuffer.restype = ctypes.c_int
_PyObject_AsWriteBuffer.argtypes = [ctypes.py_object,
                                  ctypes.POINTER(ctypes.c_void_p),
                                  ctypes.POINTER(Py_ssize_t)]

SKELETON_COLORS = [THECOLORS["red"], 
                   THECOLORS["blue"], 
                   THECOLORS["green"], 
                   THECOLORS["orange"], 
                   THECOLORS["purple"], 
                   THECOLORS["yellow"], 
                   THECOLORS["violet"]]

LEFT_ARM = (JointId.ShoulderCenter, 
            JointId.ShoulderLeft, 
            JointId.ElbowLeft, 
            JointId.WristLeft, 
            JointId.HandLeft)
RIGHT_ARM = (JointId.ShoulderCenter, 
             JointId.ShoulderRight, 
             JointId.ElbowRight, 
             JointId.WristRight, 
             JointId.HandRight)
LEFT_LEG = (JointId.HipCenter, 
            JointId.HipLeft, 
            JointId.KneeLeft, 
            JointId.AnkleLeft, 
            JointId.FootLeft)
RIGHT_LEG = (JointId.HipCenter, 
             JointId.HipRight, 
             JointId.KneeRight, 
             JointId.AnkleRight, 
             JointId.FootRight)
SPINE = (JointId.HipCenter, 
         JointId.Spine, 
         JointId.ShoulderCenter, 
         JointId.Head)

# ===============================================================================================
# define some funciton 


def draw_skeletons(skeletons):
    for index, data in enumerate(skeletons):
        # draw the Head
        RightPos = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristRight], dispInfo.current_w, dispInfo.current_h) 
        pygame.draw.circle(screen, SKELETON_COLORS[index], (int(RightPos[0]), int(RightPos[1])), 20, 0)
        LeftPos = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristLeft], dispInfo.current_w, dispInfo.current_h)
        pygame.draw.circle(screen, SKELETON_COLORS[index], (int(LeftPos[0]), int(LeftPos[1])), 20, 0)
        # pygame.display.update() 



def surface_to_array(surface):
   buffer_interface = surface.get_buffer()
   address = ctypes.c_void_p()
   size = Py_ssize_t()
   _PyObject_AsWriteBuffer(buffer_interface,
                          ctypes.byref(address), ctypes.byref(size))
   bytes = (ctypes.c_byte * size.value).from_address(address.value)
   bytes.object = buffer_interface
   return bytes

# retrieve depth from kinect
def depth_frame_ready(frame):

    if video_display:
        return

    with screen_lock:
        address = surface_to_array(screen)
        frame.image.copy_bits(address)
        del address
        # if skeletons is not None and draw_skeleton:
        #     draw_skeletons(skeletons)

        pygame.display.update()    

# retrieve video from kinect
def video_frame_ready(frame):

    if not video_display:
        return

    with screen_lock:
        address = surface_to_array(screen)
        frame.image.copy_bits(address)
        del address
        if skeletons is not None and draw_skeleton:
            draw_skeletons(skeletons)

        #aaaa
        pygame.draw.line(screen, SKELETON_COLORS[0], (0, 200),(1280, 200), 5)
        pygame.draw.line(screen, SKELETON_COLORS[0], (0, 824),(1280, 824), 5)
        pygame.draw.line(screen, SKELETON_COLORS[0], (200, 0),(200, 960), 5)
        if len(points)>1 :
                    pygame.draw.lines(screen, (0xFF, 0x00, 0x00), False, points, 2)
        
        pygame.display.update()
        
def detect_person_index(skeletons, position) :

    # define variables
    person_index = []

    for index, data in enumerate(skeletons):
        WristRight = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristRight], dispInfo.current_w, dispInfo.current_h) 
        wristright_y  = int(WristRight[1])

        if wristright_y != 0 :
            person_index.append(index)

        if len(position[index]) == 1 and wristright_y != 0 :
            position[index][0] = wristright_y
        elif len(position[index]) == 0 and wristright_y != 0 :
            position[index].append(wristright_y)
     
    return person_index

def game_start(skeletons, person_index, position) :
    global game_mode
    for index, data in enumerate(skeletons):
        WristLeft = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristLeft], dispInfo.current_w, dispInfo.current_h) 
        wristletf_y  = int(WristLeft[1])
        if index in person_index :
            if (wristletf_y < 200) :
                game_mode = True
    return game_mode

def game_end(skeletons, person_index, position) :
    global game_mode
    for index, data in enumerate(skeletons):
        WristLeft = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristLeft], dispInfo.current_w, dispInfo.current_h) 
        wristletf_y  = int(WristLeft[1])
        if index in person_index :
            if (wristletf_y > 200) :
                game_mode = False
    return game_mode

def clean_points(skeletons, person_index, position, points) :
    for index, data in enumerate(skeletons):
        WristLeft = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristLeft], dispInfo.current_w, dispInfo.current_h) 
        wristletf_y  = int(WristLeft[1])
        if index in person_index :
            if (wristletf_y > 760) :
                del points[0:len(points)]
    return points

def screenshot(skeletons, person_index, position, num) :
    for index, data in enumerate(skeletons):
        WristLeft = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristLeft], dispInfo.current_w, dispInfo.current_h) 
        wristletf_x  = int(WristLeft[0])
        if index in person_index :
            if (wristletf_x < 200) :

                pygame.image.save(screen,"screenshot_"+str(num)+".jpg")
                num += 1
    return num

def draw_line(skeletons,person_index, position,points):
    for index, data in enumerate(skeletons):
        WristRight = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristRight], dispInfo.current_w, dispInfo.current_h) 
        WristLeft = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristLeft], dispInfo.current_w, dispInfo.current_h) 

        if index in person_index :

            points.append((int(WristRight[0]), int(WristRight[1])))
            #print(points)
                

        
        #pygame.display.update() 
    return points

if __name__ == '__main__':
    global game_mode ,person_index,num
    full_screen = False
    draw_skeleton = True
    video_display = True
    game_mode = False
    position = [[]] * 6
    person_index = []
    points = []
    num = 0

    screen_lock = thread.allocate()

    screen = pygame.display.set_mode(WINSIZE,0,32)    
    pygame.display.set_caption('Python Kinect Demo')
    skeletons = None
    screen.fill(THECOLORS["black"])

    kinect = nui.Runtime()
    kinect.skeleton_engine.enabled = True
    def post_frame(frame):
        try:
            pygame.event.post(pygame.event.Event(KINECTEVENT, skeletons = frame.SkeletonData))
        except:
            # event queue full
            pass

    kinect.skeleton_frame_ready += post_frame
    
    # kinect.depth_frame_ready += depth_frame_ready    
    kinect.video_frame_ready += video_frame_ready    
    
    kinect.video_stream.open(nui.ImageStreamType.Video, 3, nui.ImageResolution.Resolution1280x1024 , nui.ImageType.Color)

    # main game loop
    done = False

    while not done:

        
        e = pygame.event.wait()
        dispInfo = pygame.display.Info()

        if e.type == pygame.QUIT:
            done = True
            break
        

        # retireve skeletons dataS
        if e.type == KINECTEVENT : # and not game_mode:
            skeletons = e.skeletons
        
            clean_points(skeletons,person_index, position,points)
            print("printnum:",num)
            num = screenshot(skeletons,person_index, position,num)

            if not game_mode :
                person_index = detect_person_index(skeletons, position)
                game_mode = game_start(skeletons, person_index, position)
            if  game_mode :
                person_index = detect_person_index(skeletons, position)
                game_mode = game_end(skeletons, person_index, position)

        if game_mode :
            draw_line(skeletons,person_index, position,points)
            
        #clean points
        
        
        # while(game_mode and len(person_index)!=0) :

        #     if e.type == pygame.QUIT:
        #         game_mode = True
        #         break
        #     elif e.type == KINECTEVENT:
        #         for index, data in enumerate(skeletons):
        #             print("{} person\n".format(index))
        #             WristLeft = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristLeft], dispInfo.current_w, dispInfo.current_h) 
        #             WristRight = skeleton_to_depth_image(data.SkeletonPositions[JointId.WristRight], dispInfo.current_w, dispInfo.current_h) 
        #             print("left wrist is ({},{})".format(int(WristLeft[0]), int(WristLeft[1])))
        #             print("right wrist is ({},{})".format(int(WristRight[0]), int(WristRight[1])))
        #             print("==================================================")

        #     elif e.type == KEYDOWN:
        #         if e.key == K_ESCAPE:
        #             game_mode = True
        #             break

        # print("\n")
        # print("==================================================")
        key = cv2.waitKey(1)
        if key == 27: 
            done = True
            break

kinect.close()
cv2.destroyAllWindows()