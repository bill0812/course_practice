import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import *
import cv2 , json

def open_image_and_filter(filter_name,img_name,out_dir) :

    img = cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Lena Original', img)
    img_padded = np.pad(img, ((1,1), (1,1)), mode='constant')
    new_img = np.zeros(img_padded.shape)
    with open(filter_name) as f:
        data = json.load(f)

    for i in range(len(data["filter"])) :
        image_filter(np.array(data["filter"][str(i+1)]),img_padded,new_img,out_dir,i)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

def image_filter(filter_matrix,img_padded,new_img,out_dir,count):

    divide = np.sum(filter_matrix)

    if divide > 0 or divide < 0 :
        filter_matrix = filter_matrix / divide

    print("----- filter is : -----\n",filter_matrix)

    for j in range(512) :
        for k in range(512) :
                new_img[j+1,k+1] = np.dot(img_padded[j:j+3,k:k+3].flatten() , filter_matrix.flatten())
                if new_img[j+1,k+1] <= 0 :
                    new_img[j+1,k+1] = 0
                elif new_img[j+1,k+1] >= 255 :
                    new_img[j+1,k+1] = 255
                else :
                    pass

    filtered_img_show(new_img,out_dir,count)

def filtered_img_show(new_img,out_dir,count):
    new_img = new_img/255   
    cv2.imshow('Lena_Processed' + str(count), new_img)
    cv2.imwrite( (out_dir + "/" + out_dir + "_" + str(count+1) + ".jpg") , new_img*255 )
