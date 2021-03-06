# EC601_HW3
Picked Exercise 1, 2 and 4. Used "baboon.jpg" as an example for the following answers.

# Exercise 1
How does a program read the cvMat object, in particular, what is the order of the pixel structure?

A: Normally, the cvMat object will be read by using cvMatName.at(x,y). Starting from the Top-left, the matrix is orgnized in the following order:

![alt text](http://aishack.in/static/img/tut/cpp-mat.jpg)

If there are more than one elements in one entry, such as RGB channels, then the sub-elements will be accessed by using cvMatName.at(x,y)[index].

# Exercise 2

1. Tested all the input images. RGB shows images in different channels and the pictrues look different in different color channels. For example, the "baboon.jpg" has very obivious color differences on the baboon's nose. The nose is nearly white in the red channel, while it shows black in green and blue channels.

    Y is luminance. Cb and Cr are blue and red color differences, repectly. As we can see, in Cr red goes darker while in Cb blue goes darker. For other images, such as "cameraman.png", the some of output images went totally grey or black because the original images were black-and-white themselves.
    
    Hue is the tint of the color. By testing several pixels, I found that in Hue channel red pixels give small values and blue pixels give large values.

<img src="https://github.com/jhzhaofred/EC601_HW3/blob/master/images/Original.png" width = "270" height = "280" alt="Keyboard" align=center /> <img src="https://github.com/jhzhaofred/EC601_HW3/blob/master/images/Y.png" width = "270" height = "280" alt="Keyboard" align=center />

<img src="https://github.com/jhzhaofred/EC601_HW3/blob/master/images/cb.png" width = "270" height = "280" alt="Keyboard" align=center /> <img src="https://github.com/jhzhaofred/EC601_HW3/blob/master/images/cr.png" width = "270" height = "280" alt="Keyboard" align=center />

2. For values of pixel (20,25) at "baboon.jpg":

    R: 156 G: 165 B: 102 (Range: 0, 255)

    Y: 98 Cb: 129 Cr: 155 (Range: 0, 255)

    H: 165 S: 97 V: 34 (Range for H: 0, 360; Range for S, V: 0, 100)

# Exercise 4
1. Adaptive Thresholding gives the best result, Band Thresholding gives the most blurry result. Thresholded and semi-threshold gives decent details, but there results are more gray than others.
![alt text](https://github.com/jhzhaofred/EC601_HW3/blob/master/images/threshold.png)

2. Obviously, binary threshold will cause information lost because it only has one threshold value. This issue becomes more         significant when the image has complicated brightness.

3. Adaptive Thresholding is useful to deal with the issue listed above. It generates different threshold in different areas of the image so that the image will not lose much information.

# Referring
http://aishack.in/tutorials/opencvs-interface/

https://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html

https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html
