import cv2, json, os
import numpy as np

# THIS CODE IS WRITTEN UNEFFICIENTLY, BECAUSE THIS JUST FOR SHOWING RESULT 
# AND HAND IN THE TAKE HOME TEST WITH THE IMAGE

# this is for the first question "start"
def question_1() :
    # read image and toward fft the image to frequency domain for three questions
    # and set difference image
    bridge = cv2.imread("bridge.jpg",0)
    bridge_difference = np.zeros((256,256))
    bridge_f = np.fft.fft2(bridge)
    bridge_fshift = np.fft.fftshift(bridge_f).flatten()

    # use fft to get magnitude
    magnitude_spectrum_bridge = np.abs(bridge_fshift)
    magnitude_spectrum_bridge_original = magnitude_spectrum_bridge
    magnitude_spectrum_normalized = np.log(magnitude_spectrum_bridge).reshape(bridge.shape[0],bridge.shape[1])
    magnitude_spectrum_normalized_bridge_original = (magnitude_spectrum_normalized-np.min(magnitude_spectrum_normalized))/(np.max(magnitude_spectrum_normalized)-np.min(magnitude_spectrum_normalized))

    # use fft to get phase
    phase_bridge = np.angle(bridge_fshift)

    # sort the coefficients
    magnitude_spectrum_bridge  = np.argsort(magnitude_spectrum_bridge)
    magnitude_spectrum_bridge_max = magnitude_spectrum_bridge[int((len(magnitude_spectrum_bridge))*3/4):]

    # keep the largest 1/4 coefficients
    for i in range(len(magnitude_spectrum_bridge)) :
        if i in magnitude_spectrum_bridge_max :
            pass
        else :

            # set up for 1 just for observing the spectrum before and after
            # i try 0 and 1, but almost no difference between this two
            magnitude_spectrum_bridge_original[i] = 0

    # view the spectrum for recover one
    image_recover_original_normalize = [np.log(value) if value > 0 else 0 for value in magnitude_spectrum_bridge_original ]
    magnitude_spectrum_normalized_bridge_new = (image_recover_original_normalize-np.min(image_recover_original_normalize))/(np.max(image_recover_original_normalize)-np.min(image_recover_original_normalize))

    # reshape the magnitude_spectrum_bridge / phase_bridge numpy array / and spectrum
    magnitude_spectrum_bridge_original = magnitude_spectrum_bridge_original.reshape(bridge.shape[0],bridge.shape[1])
    phase_bridge = phase_bridge.reshape(bridge.shape[0],bridge.shape[1])
    magnitude_spectrum_normalized_bridge_new = magnitude_spectrum_normalized_bridge_new.reshape(bridge.shape[0],bridge.shape[1])

    # use the formula to get the real number and imaginary number, then combine them
    image_recover_original = np.multiply(magnitude_spectrum_bridge_original, np.exp(1j*phase_bridge))

    # inverse fft to spatial domain
    image_recover_original = np.fft.ifftshift(image_recover_original)
    image_recover = np.fft.ifft2(image_recover_original)
    image_recover = np.real(image_recover)

    # show spectrum
    spectrum_all = np.hstack((magnitude_spectrum_normalized_bridge_original,magnitude_spectrum_normalized_bridge_new))
    cv2.imshow("Question 1/Question 1'" + 's Answers(Image A) Spectrum', spectrum_all)
    cv2.imwrite("Question 1/Question 1'" + 's Answers(Image A) Spectrum.jpg', spectrum_all*255)

    # normalize that recovered image with saving largest coefficients
    image_recover = (image_recover - np.amin(image_recover))/(np.amax(image_recover) - np.amin(image_recover))
    cv2.imwrite("Question 1/Question 1'" + 's Answers(Image A).jpg', image_recover*255)

    # caculate error with mse
    bridge_difference = (bridge/255).astype("float") - image_recover.astype("float")
    current_error_mse = np.sum(((bridge/255).astype("float") - image_recover.astype("float")) ** 2)
    current_error_mse = current_error_mse / float(256 * 256)

    return image_recover, current_error_mse , bridge_difference
# ======================================================================================

# this is for the second question "start"
def question_2() :

    # read image and toward fft the image to frequency domain for three questions
    bridge = cv2.imread("bridge.jpg",0)
    bridge_new = np.zeros(bridge.shape)

    # and set difference image
    bridge_difference = np.zeros((256,256))

    # keep the largest 1/4 coefficients
    for i in range(16) :
        for j in range(16) :

            # set up some variables
            current_pixel = list()
            current_sort, current_sort_max = list(), list()
            
            # adding current pixels
            for x in range(16) :
                for y in range(16) :
                    current_pixel.append(bridge[i*16+x][j*16+y])
            
            # here are for fourier transformation
            current_pixel = np.array(current_pixel).reshape((16,16))

            current_pixel_bridge_f = np.fft.fft2(current_pixel)
            current_pixel_bridge_fshift = np.fft.fftshift(current_pixel_bridge_f)

            # use fft to get magnitude
            magnitude_spectrum_current_pixel = np.abs(current_pixel_bridge_fshift)

            # use fft to get phase
            phase_current_pixel = np.angle(current_pixel_bridge_fshift)

            # append current 256 magnitude to list
            for x in range(16) :
                for y in range(16) :
                    current_sort.append(magnitude_spectrum_current_pixel[x][y])

            current_sort  = np.sort(current_sort)
            current_sort_max = current_sort[int((len(current_sort))*3/4):]
            
            # find 1/4 largest
            for x in range(16) :
                for y in range(16) :
                    if magnitude_spectrum_current_pixel[x][y] in current_sort_max :
                        pass
                    else :
                        magnitude_spectrum_current_pixel[x][y] = 0
    
            # use the formula to get the real number and imaginary number, then combine them
            image_recover_current = np.multiply(magnitude_spectrum_current_pixel, np.exp(1j*phase_current_pixel))

            # inverse fft to spatial domain
            image_recover_current = np.fft.ifftshift(image_recover_current)
            image_recover_current = np.fft.ifft2(image_recover_current)
            image_recover_current = np.real(image_recover_current)

            # normalize that recovered image with saving largest coefficients
            # image_recover_current = (image_recover_current - np.amin(image_recover_current))/(np.amax(image_recover_current) - np.amin(image_recover_current))
            
            # recover image to new one
            for x in range(16) :
                for y in range(16) :
                    bridge_new[i*16+x][j*16+y] = image_recover_current[x][y]

    # normalize that recovered image with saving largest coefficients
    bridge_new = (bridge_new - np.amin(bridge_new))/(np.amax(bridge_new) - np.amin(bridge_new))
    cv2.imwrite("Question 1/Question 2'" + 's Answers(Image B).jpg', bridge_new*255)

    # caculate error with mse
    bridge_difference = (bridge/255).astype("float") - bridge_new.astype("float")
    current_error_mse = np.sum(((bridge/255).astype("float") - bridge_new.astype("float")) ** 2)
    current_error_mse = current_error_mse / float(256 * 256)

    return bridge_new, current_error_mse , bridge_difference
# ======================================================================================

# this is for the third question "start"
def question_3() :
    # read image and toward fft the image to frequency domain for three questions
    bridge_original = cv2.imread("bridge.jpg",0)
    bridge_resize = np.zeros((128,128))

    # and set difference image
    bridge_difference = np.zeros((256,256))

    # bridge_resize = cv2.resize(bridge_original, (128, 128))
    # using average method by my own, instead of function
    for i in range(128) :
        for j in range(128) :
            
            # if using this way below, it will go wrong, it's programming grammarly mistake
            # print(bridge_original[i*2:2*(i+1)][j*2:2*(j+1)])

            # use this
            bridge_resize[i][j] = np.mean(bridge_original[i*2:(i+1)*2,j*2:(j+1)*2])

    bridge_f = np.fft.fft2(bridge_resize)
    bridge_fshift = np.fft.fftshift(bridge_f)
    bridge_fshift_padded = np.pad(bridge_fshift, ((64,64), (64,64)), mode='constant')

    # inverse fft to spatial domain
    image_recover = np.fft.ifftshift(bridge_fshift_padded)
    image_recover = np.fft.ifft2(image_recover)
    image_recover = np.real(image_recover)
    
    # normalize that recovered image with saving largest coefficients
    image_recover = (image_recover - np.amin(image_recover))/(np.amax(image_recover) - np.amin(image_recover))
    cv2.imwrite("Question 1/Question 3'" + 's Answers(Image C).jpg', image_recover*255)

    # caculate error with mse
    bridge_difference = (bridge_original/255).astype("float") - image_recover.astype("float")
    current_error_mse = np.sum(((bridge_original/255).astype("float") - image_recover.astype("float")) ** 2)
    current_error_mse = current_error_mse / float(256 * 256)

    return image_recover, current_error_mse , bridge_difference
# ======================================================================================

if __name__ == "__main__":

    # create folder
    if not os.path.exists("Question 1") :
        os.makedirs("Question 1")

    # declare some variables
    # define error
    error_dict = dict()
    error_dict["Error"] = dict()

    # show all answer and show MSE
    bridge = cv2.imread("bridge.jpg",0)
    image_recover_1, current_error_mse_1 , bridge_difference_1 = question_1()
    image_recover_2, current_error_mse_2 , bridge_difference_2 = question_2()
    image_recover_3, current_error_mse_3 , bridge_difference_3 = question_3()

    img_combine_all = np.hstack((bridge/255,image_recover_1,image_recover_2,image_recover_3))
    difference_combine_all = np.hstack((bridge_difference_1,bridge_difference_2,bridge_difference_3))
    
    # show image and save
    cv2.imshow("Question 1'" + 's Answers', img_combine_all)
    cv2.imshow("Question 1'" + 's Answers Difference', difference_combine_all)
    cv2.imwrite("Question 1/Question 1'" + 's All Answers.jpg', img_combine_all*255)
    cv2.imwrite("Question 1/Question 1'" + 's All Answers Difference.jpg', difference_combine_all*255)

    print("MSE Error : {\n\tQuestion 1(Image A with Original One) : %.10f,\n\tQuestion 2(Image B with Original One) : %.10f,\n\tQuestion 3(Image C with Original One) : %.10f,\n}" %(current_error_mse_1,current_error_mse_2,current_error_mse_3))
    
    # save result
    error_dict["Error"]["Question 1(Image A with Original One)"] = current_error_mse_1
    error_dict["Error"]["Question 2(Image B with Original One)"] = current_error_mse_2
    error_dict["Error"]["Question 3(Image C with Original One)"] = current_error_mse_3

    # write error file
    with open("Question 1/Question 1's Error.json", 'w') as outfile:
        json.dump(error_dict, outfile)

    # wait for ESC key to exit
    if cv2.waitKey(0) == 27:         
        cv2.destroyAllWindows()