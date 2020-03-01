import cv2
import numpy as np
import matplotlib.pyplot as plt

def mse(img1,img2):
	mse = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
	mse /= float(img1.shape[0] * img1.shape[1])
	return mse
	
def fft_image(img):
	f = np.fft.fft2(img)
	magnitude = np.abs(f)
	phase = np.angle(f)
	largest = np.sort(magnitude.reshape(-1))[int(img.size * 0.75)]
	magnitude_lar = (magnitude >= largest) * magnitude
	f_inv = magnitude_lar * np.exp(1j * phase)
	img_inv = np.fft.ifft2(f_inv)
	img_inv = np.real(img_inv)
	return img_inv

def seg_image(img):
    img2 = np.zeros((256,256))
    for i in range(0,16):
	    for j in range(0,16):
			#16*i行到(i+1)*16行的第16*j到(j+1)*16列
			img2[16*i:16*(i+1), 16*j:16*(j+1)] = fft_image(img[16*i:16*(i+1), 16*j:16*(j+1)])
    return img2	

def pad_with(vector, pad_width, iaxis, kwargs):
	pad_value = kwargs.get('padder', 0)
	vector[:pad_width[0]] = pad_value
	vector[-pad_width[1]:] = pad_value
	return vector
	
def res_image(img):
	res_img = np.zeros((128, 128)) 
	for i in range(0,128):
		for j in range(0, 128):
			res_img[i, j] = np.mean(img[2*i:2*(i+1),2*j:2*(j+1)]) 
	f = np.fft.fft2(res_img)
	fshift = np.fft.fftshift(f)
	imgC = np.pad(fshift, fshift.shape[0] / 2, pad_with)
	imgC = np.abs(np.fft.ifft2(imgC)) * 4
	return imgC
	

#第一題
img = cv2.imread('bridge.jpg',0)

#imageA
imgA = fft_image(img)
#imageB
imgB = seg_image(img)
#imageC
imgC = res_image(img)
#MSE
mse_A = mse(img,imgA)
mse_B = mse(img,imgB)
mse_C = mse(img,imgC)
print("MSE(image, imageA)=", mse_A)
print("MSE(image, imageB)=", mse_B)
print("MSE(image, imageC)=", mse_C)

plt.imshow(img, cmap = 'gray')
plt.show()
plt.imshow(imgA, cmap = 'gray')
plt.show()
plt.imshow(imgB, cmap = 'gray')
plt.show()
plt.imshow(imgC, cmap = 'gray')
plt.show()


#第二題
img2 = cv2.imread('Fig0514.jpg',0)

median_3 = cv2.medianBlur(img2, 3)
median_5 = cv2.medianBlur(img2, 5)
median_7 = cv2.medianBlur(img2, 7)

plt.imshow(img2, cmap = 'gray')
plt.show()
plt.imshow(median_3, cmap = 'gray')
plt.show()
plt.imshow(median_5, cmap = 'gray')
plt.show()
plt.imshow(median_7, cmap = 'gray')
plt.show()


