import cv2
import numpy as np

# getting the images

#img = cv2.imread('opencv1.jpeg')
img1 = cv2.imread('opencv2.png')
# setting the ranges:

#  red done
lower_red = np.array([0,0,199])      # [0,0,195] # [0,0,218]
upper_red = np.array([160,245,255])   # [160,240,255]
mask1 = cv2.inRange(img1, lower_red, upper_red)

#cv2.imshow('original',img)

red = cv2.bitwise_and(img1, img1, mask=mask1)
red[np.where((red==[0,0,0]).all(axis=2))]=[255,255,255]


###   green done --- [0,100,0]  and [50,255,200]

lower_green = np.array([0,100,0])   # 0,50,0  # 0,100,0
upper_green = np.array([50,255,200])   # 90,255,50    # 200, 255, 50 -- some blue shades appear of python

mask2 = cv2.inRange(img1, lower_green, upper_green)

# blue done -- [50,0,0] and  [255,200,85]

lower_blue = np.array([50,0,0])   # 50,0,0
upper_blue = np.array([255,200,85])    # 255,200,85
mask3 = cv2.inRange(img1, lower_blue, upper_blue)
green = cv2.bitwise_and(img1, img1, mask=mask2)
blue = cv2.bitwise_and(img1, img1, mask=mask3)
blue[np.where((blue==[0,0,0]).all(axis=2))]=[255,255,255]
green[np.where((green==[0,0,0]).all(axis=2))]=[255,255,255]

cv2.imshow("mask1", mask1)
cv2.imshow('green',green)
cv2.imshow('blue', blue)
cv2.imshow('red', red)
cv2.imshow('img1',img1)
#cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
