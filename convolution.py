
import numpy as np
import cv2
from PIL import Image

def convolution(image, kernel):            #function for convolution
    
    height, width = image.shape            #finding height and width of the image
                                           
    new_image = np.zeros_like(image)       #initializing a random image
    '''
    Here padding is not done. so convolution is done from the pixel in 2nd row and 2nd column. 
    ie., the pixels in the boundaries are kept 0 only.

    '''

    for i in range(1,height-1):            #starting from 2nd row
        for j in range(1,width-1):         #starting from 2nd column
            
            value = 0                      #initialising a random variable to 0
            
            for k in range(3):             #looping the kernal
                for l in range(3):
                    value += kernel[k, l] * image[i + k - 1, j + l - 1]
            
            new_image[i, j] = max(0, value)       #if value is negative, it is considered as 0

    return new_image

def main():
    image = cv2.imread('Einstein.jpg')
    img=image[:,:,0]          #red component of image
    img1=image[:,:,1]         #green component of image
    img2=image[:,:,2]         #blue component of image
    
    kernel = np.array([[1/16,1/8,1/16],
                       [1/8,1/4,1/8],
                       [1/16,1/8,1/16]])     #change the kernal accordingly

    result1 = convolution(img, kernel)      #convolving the red component of image
    result2 = convolution(img1, kernel)     #convolving the green component of image
    result3 = convolution(img2, kernel)     #convolving the blue component of image
    
    rgb=np.dstack((result3,result2,result1))       #stacking the three layers of image
    
    img=Image.fromarray(rgb)                       
    img.show()                                     #displaying the image
   
    '''
    print("\n red")
    print(rgb[:,:,0])
    print("\n green")
    print(rgb[:,:,1])
    print("\n blue")
    print(rgb[:,:,2])
'''

if __name__ == "__main__":
    main()
