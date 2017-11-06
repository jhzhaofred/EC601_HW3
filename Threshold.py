# Copyright 2017 Jiahao Zhao jiahao1@bu.edu

import cv2
from matplotlib import pyplot as plt
import sys

# Usage: 
# For example: $ python Threshold.py /Test_images/baboon.jpg

try:
	filename = sys.argv[1]
except:
	print("There is no input image.")
	print("Usage: $ python Threshold.py <input image>")
	exit(1)
img = cv2.imread(filename,1)

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow('Input Image',img)

 # 0: Binary,      1: Binary Inverted,      2: Threshold Truncated,      3: Threshold to Zero,      4: Threshold to Zero Inverted    
  
threshold_type = 2
threshold_value = 128

#Usage:
# img = cv2.imread('gradient.png',0)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

ret, dst = cv2.threshold(gray, threshold_value, 255, threshold_type)

cv2.imshow('Thresholded image',dst)

current_threshold = 128
max_threshold = 255


ret, thresholded = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY)

cv2.imshow('Binary threshold',thresholded)

# band thresholding
threshold1 = 27
threshold2 = 125

ret, t1 = cv2.threshold(gray, threshold1, max_threshold, cv2.THRESH_BINARY)
ret, t2 = cv2.threshold(gray, threshold2, max_threshold, cv2.THRESH_BINARY_INV)

t3 = t1 & t2

cv2.imshow('Band Thresholding',t3)

# Semi thresholding
ret, semi_thresholded_image = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY_INV)
semi_thresholded_image = gray & semi_thresholded_image
#bitwise_and( gray, semi_thresholded_image, semi_thresholded_image );
cv2.imshow('Semi Thresholding', semi_thresholded_image)

# Adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)

print("Close images to continue...")
cv2.waitKey(0)