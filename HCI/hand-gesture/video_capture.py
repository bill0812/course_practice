import numpy as np
import cv2
import os
import glob as glob

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 60)
out = None

# 設定影像的尺寸大小
cv2.namedWindow('My Window',cv2.WINDOW_KEEPRATIO)
cv2.setWindowProperty('My Window',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

fgbg = cv2.createBackgroundSubtractorMOG2()

image_dir = "screenshots/"
video_dir = "videohots/"

if not os.path.isdir(image_dir):
    os.makedirs(image_dir)
screenshot_count = len(glob.glob(image_dir + '.jpeg'))

if not os.path.isdir(video_dir):
    os.makedirs(video_dir)
video_count = len(glob.glob(video_dir + '.mp4'))

def find_specific_contours(fgmask, start, end, kind):

    contours, hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    result = []
    area = 0
    for each_cont in contours:
        
        center_x = 0
        center_y = 0
        count = 0
        result_tmp = []

        for x_y in each_cont :

            x_y[0][0] = np.clip(x_y[0][0], start[0], end[0])
            x_y[0][1] = np.clip(x_y[0][1], start[1], end[1])
            
            center_x += x_y[0][0]
            center_y += x_y[0][1]

            result_tmp.append([x_y[0][0],x_y[0][1]])

            count += 1

        center_x = center_x//count
        center_y = center_y//count
        
        if start[0] < center_x < end[0] and start[1] < center_y < end[1] :

            result_tmp = np.array(result_tmp)
            if cv2.contourArea(result_tmp) < 3000 :
                continue

            area += cv2.contourArea(result_tmp)
            result.append(result_tmp)

    return result, area

prev, current, count, status, start_time = 0, 0, 0, 0, 0
while(1):
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    frame_text = frame

    fgmask = fgbg.apply(frame)

    # or
    width = cap.get(3)  # float
    height = cap.get(4) # float
    each_block_width = int(width//4)
    each_block_height = int(height//3)

    if count == 0 :
        prev = fgmask
        current = fgmask
    else :
        prev = current
        current = fgmask
    
    prev = cv2.GaussianBlur(prev,(7,7),0)
    current = cv2.GaussianBlur(current,(7,7),0)

    fgmask = cv2.absdiff(prev, current)
    ret, fgmask = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)

    # 造成視覺上影片太慢，所以拿掉
    fgmask = cv2.bilateralFilter(fgmask,9,75,75)
    # fgmask = cv2.fastNlMeansDenoising(fgmask, None, 9, 13)
    fgmask = cv2.dilate(fgmask, None, iterations=1)

    # upper left
    cv2.rectangle(frame,(20,20),(each_block_width+20,each_block_height+20),(0,255,0),3)

    # upper right
    cv2.rectangle(frame,(int(width)-20, 20),(int(width)-(each_block_width+20),each_block_height+20),(255,0,0),3)

    # find Contours
    contours_upper_left, area_upper_left = find_specific_contours(fgmask, (20,20), (each_block_width+20,each_block_height+20),0)
    contours_upper_right, area_upper_right = find_specific_contours(fgmask, ((int(width)-(each_block_width+20)), 20), ((int(width)-20),each_block_height+20),1)

    if area_upper_left > area_upper_right :
        
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.drawContours(frame, contours_upper_left, -1, (0,0,255), 3)
        frame_text = cv2.putText(frame_text, "Start Recording",(int(20),int(height-10)),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),5)
        if out == None :
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(video_dir + 'oputput' + str(video_count) + '.mp4', fourcc, 29.97, (1280, 720))
        
        out.write(frame)

    # screenshot
    elif area_upper_right > area_upper_left :
        
        cv2.drawContours(frame, contours_upper_right, -1, (0,0,255), 3)
        frame_text = cv2.putText(frame_text, "Taking Pictures",(int(20),int(height-10)),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),5)
        cv2.imwrite(image_dir + str(screenshot_count) + ".jpeg", frame)
        screenshot_count += 1

    else :
        pass
                
    fgmask = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)

    count += 1
    final = cv2.vconcat([frame_text, fgmask])
    cv2.imshow('My Window',final)

    # exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()