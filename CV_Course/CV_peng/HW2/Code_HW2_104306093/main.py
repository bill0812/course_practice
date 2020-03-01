import histogram_equalization_grayscale as gray
from argparse import ArgumentParser
import json, os
import cv2 as cv
import numpy as np

if __name__ == "__main__" :
    parser = ArgumentParser('Answer To The Homework 3 :  \n1) Binary Morphological Operations.\n2) Histogram Equalization\n3)About Some Contrast Enhancement Techniques')
    parser.add_argument('--question', required = True, type=int , choices = [1,2,3], dest="question", help="Input your question's number.")
    args = parser.parse_args()
    question = args.question

    if question == 1 :

        # create folder if not exsist
        if not os.path.exists("text-broken") :
            os.makedirs("text-broken")

        # read image in gray scale
        img = cv.imread("text-broken.tif",cv.IMREAD_GRAYSCALE) 

        # using basic kernel 
        kernel_3 = np.ones((3,3),np.uint8)
        kernel_5 = np.ones((5,5),np.uint8)
        kernel_7 = np.ones((7,7),np.uint8)

        # do morphologyEx operation of "CLOSE" - closing and "GRADIENT" - finding boundary
        # using kernel for 5*5 for closing is better, and boundary for 3*3 is quite good
        closing_img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel_5)
        boundary_img = cv.morphologyEx(closing_img, cv.MORPH_GRADIENT, kernel_3)
        
        # show image and save
        combine_two = np.hstack((closing_img,boundary_img))
        cv.imshow("text-broken ( original / closing / boundary",combine_two)
        cv.imwrite("text-broken/closing_and_boundary.jpg",combine_two)

        # wait key and wait push "ESC" key
        if cv.waitKey(0) & 0xFF == ord('q'):
            cv.destroyAllWindows()

    elif question == 2 :
        img_name = "aerialview-washedout.tif"
        out_dir = "aerialview-washedout"

        # create folder if not exsist
        if not os.path.exists(out_dir) :
            os.makedirs(out_dir)

        gray.process_histogram_mine(img_name,out_dir)
    elif question == 3 :
        img_name = "einstein-low-contrast.tif"
        out_dir = "einstein-low-contrast"

        # create folder if not exsist
        if not os.path.exists(out_dir) :
            os.makedirs(out_dir)

        # get image 
        img = cv.imread(img_name,cv.IMREAD_GRAYSCALE) 
        height, width = img.shape[0] , img.shape[1]

        # first way is Histogram Equalization
        # using opecv tool to equalizeHist
        opencv_equ = cv.equalizeHist(img)

        # Second Way is CLAHE which mentioned in class
        # create a CLAHE object (Arguments are optional)
        clahe = cv.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        clahe_transform = clahe.apply(img)  

        # Third Way is Gamma Correlation which also mentioned in class
        # set up a match table for correlation
        gamma_value = 0.7
        invGamma = 1.0 / gamma_value
        table = np.zeros(256, np.uint8)
        for i in range(0, 256) :
            table[i] = np.array(((i/255.0)**invGamma)*255)

        # apply gamma correction using the lookup table
        final_gamma =  cv.LUT(img, table)

        # show image and save
        combine_four = np.hstack((img,opencv_equ,final_gamma,clahe_transform))
        cv.imshow("Compare Three Ways ( HE / Gamma Correlation / CLAHE )",combine_four)
        cv.imwrite("einstein-low-contrast/Comapre-Four-Ways.jpg",combine_four)
        
        # wait key and wait push "ESC" key
        if cv.waitKey(0) & 0xFF == ord('q'):
            cv.destroyAllWindows()     
    else :
        parser.error("Choice is Wrong ( only 1 to 3 ) !!")
