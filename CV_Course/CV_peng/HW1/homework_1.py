import cv2 as cv
import numpy as np

# read image
img_left = cv.imread('laptop_left.png')
img_right = cv.imread('laptop_right.png') 
img_lena = cv.imread('lena_flipped.jpg') 

# 1. By numpy's append funciton
images_laptop = np.append(img_left,img_right , axis=1)

# 2. By numpy's concatenate funciton
# images_laptop = np.concatenate([img_left, img_right ], axis=1)

# vertically flipped the lena image
img_lena_flipped = cv.flip(img_lena, 0)

# write and show image for question 1 & 2
cv.imwrite('output_laptop.jpg', images_laptop)
cv.imwrite("lena_normal.jpg", img_lena_flipped)
cv.imshow('output_laptop', images_laptop)

# read lena normal one and transfer to ycbcr
img_lena = cv.imread('lena_normal.jpg')
lena_ycbcr = cv.cvtColor(img_lena, cv.COLOR_BGR2YCrCb)
lena_y, lena_cr, lena_cb = cv.split(lena_ycbcr)
lena_cr_new = np.zeros(lena_cr.shape)
lena_cb_new = np.zeros(lena_cb.shape)

# make original 4:4:4 to 4:2:0 for cr and cb
# we all know the images is 512 * 512
# if not , we need to cut the image to even number size
for i in range(0,512,2) :
    for j in range(0,512,2) :
        replace_val_cr = int(int(lena_cr[i,j]) + int(lena_cr[i,j+1]) + int(lena_cr[i+1,j]) + int(lena_cr[i+1,j+1]))/4
        replace_val_cb = int(int(lena_cb[i,j]) + int(lena_cb[i,j+1]) + int(lena_cb[i+1,j]) + int(lena_cb[i+1,j+1]))/4
        lena_cr_new[i,j] = replace_val_cr
        lena_cr_new[i,j+1] = replace_val_cr
        lena_cr_new[i+1,j] = replace_val_cr
        lena_cr_new[i+1,j+1] = replace_val_cr

        lena_cb_new[i,j] = replace_val_cb
        lena_cb_new[i,j+1] = replace_val_cb
        lena_cb_new[i+1,j] = replace_val_cb
        lena_cb_new[i+1,j+1] = replace_val_cb

# merge new ycbcr
lena_new = cv.merge([lena_y,lena_cr_new.astype(np.uint8),lena_cb_new.astype(np.uint8)])

# combine all three channels to one image frame
lena_ycbcr_each = np.hstack((lena_y,lena_cr,lena_cb))
lena_ycbcr_new_old = np.hstack((img_lena_flipped,lena_ycbcr,lena_new))

# write and show image for question 3
cv.imshow('lena_ycbcr_new_old', lena_ycbcr_new_old)
cv.imshow('lena_ycbcr_each', lena_ycbcr_each)
cv.imwrite('lena_ycbcr_each.jpg', lena_ycbcr_each)
cv.imwrite('lena_ycbcr_new_old.jpg', lena_ycbcr_new_old)

# wait for ESC key to exit
if cv.waitKey(0) == 27:         
    cv.destroyAllWindows()