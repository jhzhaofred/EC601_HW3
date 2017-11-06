# Copyright 2017 Jiahao Zhao jiahao1@bu.edu
import cv2
import numpy as np
import sys

try:
	filename = sys.argv[1]
except:
	print("There is no input image.")
	print("Usage: $ python ColorImage.py <input image>")
	exit(1)
img = cv2.imread(filename)

# print(filename)
b,g,r = cv2.split(img);

cv2.imshow('Original',img);
cv2.imshow('Red',r);
cv2.imshow('Green',g);
cv2.imshow('Blue',b);

# print ("RGB:")
# print ("R: %d, G: %d, B: %d" %(img[20][25][2],img[20][25][1],img[20][25][0]))

ycrcb_image = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
y,cb,cr = cv2.split(ycrcb_image);

cv2.imshow('Y',y);
cv2.imshow('Cr',cr);
cv2.imshow('Cb',cb);

# print ("YCrCb:")
# print ("Y: %d, Cr: %d, Cb: %d" %(ycrcb_image[20][25][2],ycrcb_image[20][25][1],ycrcb_image[20][25][0]))

hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_image);

cv2.imshow('H',h);
cv2.imshow('S',s);
cv2.imshow('V',v);

# print ("HSV:")
# print ("H: %d, S: %d, V: %d" %(hsv_image[20][25][2],hsv_image[20][25][1],hsv_image[20][25][0]))
print("Close images to continue...")
cv2.waitKey(0)
