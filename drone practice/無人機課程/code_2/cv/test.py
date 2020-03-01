import cv2
import numpy as np

# def findMask(img):
#   lower_red_0 = np.array([0, 70, 0]) 
#   upper_red_0 = np.array([5, 255, 255])
#   lower_red_1 = np.array([175, 70, 0]) 
#   upper_red_1 = np.array([180, 255, 255])
#   red_mask0 = cv2.inRange(hsv_img, lower_red_0, upper_red_0)
#   red_mask1 = cv2.inRange(hsv_img, lower_red_1, upper_red_1)
#   red_mask = cv2.bitwise_or(red_mask0, red_mask1) 
#   return red_mask0
  
img = cv2.imread('red.jpg')
# fourcc = cv2.VideoWriter_fourcc('X',"V",'I','D')
# out = cv2.VideoWriter('test.avi', fourcc, 20.0,(img.shape[1], img.shape[0]))
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # red hsv range and mask on hsv_img
# red_mask = findMask(hsv_img)
# cv2.imshow("red_mask",red_mask)
cv2.imshow("img",img)
# contour_contours, contour_h = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contour_i = red_mask.copy()
# contour_i = cv2.cvtColor(contour_i, cv2.COLOR_GRAY2BGR)
# cv2.drawContours(contour_i, contour_contours, -1, (0, 0, 255), 2)
# cv2.imshow("red_mask",contour_i)
# # show red mask
# avg_x = []
# avg_y = []
# for cnt in contour_contours:
#   print(cnt)
#   for c in cnt:
#     avg_x.append(c[0][0])
#     avg_y.append(c[0][1])
# print(np.mean(avg_x))
# print(np.mean(avg_y))
# cv2.circle(contour_i, (int(np.mean(avg_x)), int(np.mean(avg_y))), 10, (0,0,255), 10)
# cv2.imshow("test_center", contour_i)
# cv2.imwrite("test_center.jpg", contour_i)

# frame = 600
# while frame > 0:
#   print(frame)
#   contour_i = cv2.flip(contour_i,0)
#   out.write(contour_i)
#   cv2.imshow("red_mask", red_mask) 
#   cv2.imshow("test", contour_i)
#   #cv2.imwrite("red_mask.jpg", red_mask)
#   #cv2.imwrite("test.jpg", contour_i)
#   cv2.waitKey(1)
#   frame -= 1
  
# out.release()

# if cv2.waitKey(0) & 0xFF == ord('q'):
#   cv2.destroyAllWindows()
     
# Select ROI
r = cv2.selectROI(img)
     
# Crop image
imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
 
# Display cropped image
cv2.imshow("Image", imCrop)
cv2.waitKey(0)