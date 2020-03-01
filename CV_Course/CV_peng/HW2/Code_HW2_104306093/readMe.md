## This is a brief discription of homework 2
---

## 👉 Some output by experiments : 

| Question | Result |
| :---: | :---: |
| `Question 1's Image` | ![](https://i.imgur.com/RiZQSFQ.jpg) | 
| `Question 2's Image`  | ![](https://i.imgur.com/zB8Q0UB.jpg) |
| `Question 2's Histogram` | ![](https://i.imgur.com/HgOWchK.jpg) |
| `Question 3's Image`  | ![](https://i.imgur.com/boueTC1.jpg) |

---
## 👉 Let's have some discussion

* For first question, we use the opencv tool to make each character in the image closed, and also use that closed image to find boundary of each character.

    + For closing operation, we use __「 morphologyEx 」__ funciton, and match the __「 cv.MORPH_CLOSE 」__ and __「 kernel with 5*5 」__ to close each character in the image.

     + For finding boundaries, we also use __「 morphologyEx 」__ funciton, and match the __「 cv.MORPH_GRADIENT 」__ and __「 kernel with 3*3 」__ to find each character's boundary in the image.

* For second question : 

    + we first find the histogram, then use the __「 for loop 」__ to caculate the amount of each value ( 1 - 255 ), and also use the __formula to equalize the histogram__. Finally, we map the value between original one and transfered one. 
    
    + Besides, we use the opencv tool __「 cv.equalizeHist 」__ to get a equalized image.

    + Having this two images from different ways, we use __「 MSE 」__ /  __「 RMSE 」__ to calculate the error ( loss ) between the two, and output the __json file__

* For third question, we use different to compare different output :

    + First is __「 Histogram Equaliztion 」__, using the opencv tool to show the output

    + Second is __「 Gamma Correlation  」__, which teacher mentioned in class before. And we using the map table to transform the original histogram ( original value ). And for the value "Gamma", we choose 0.7 which I thought the result is better among all

    + Third, we also use the concept that teacher also mentioned in class before, which called __「 CLAHE ( Contrast Limited Adaptive Histogram Equalization ) 」__, by using the opencv tool to get the oupt. And for the parameters, one is "clipLimit" which I set 3.0 ; one is "tileGridSize", which I choose (8,8).And as for the purpose of setting this two parameters, we can see the paper, and understand those two :

        
        - Clip Limit : 
        
            ![](https://i.imgur.com/RCTFElY.png)
        
        - Tile Grid Size :
        
            ![](https://i.imgur.com/zHlEz6u.png)

    + After those three method, we combine four images, and compare to each one, I found that the image from the third method is much better than other. That means, it shows more detail of the images and more clear than others.

---
## 👉 Here are some file and directory

* [text-broken](text-broken/) :

    + [closing_and_boundary.jpg](text-broken/closing_and_boundary.jpg)


* [aerialview-washedout](aerialview-washedout/) :

    + [compare_each.jpg](aerialview-washedout/compared_each.jpg)

    + [compared_histogram_each.jpg](aerialview-washedout/histogram.jpg)

    + [error.json](aerialview-washedout/error.json)

* [einstein-low-contrast](einstein-low-contrast/) :

    + [einstein-low-contrast](einstein-low-contrast/Comapre-Four-Ways.jpg)

---

##  ✨ So, This is a simple discription of homework 2 ✨ 

###### tags: `Image Processing`