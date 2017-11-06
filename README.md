# EC601_HW3
# Exercise 1
How does a program read the cvMat object, in particular, what is the order of the pixel structure?

A: Normally, the cvMat object will be read by using cvMatName.at(x,y). Starting from the Top-left, the matrix is orgnized in the following order:

![alt text](http://aishack.in/static/img/tut/cpp-mat.jpg)

If there are more than one elements in one entry, such as RGB channels, then the sub-elements will be accessed by using cvMatName.at(x,y)[index].

# Exercise 2

1. Tested all the input images. RGB shows images in different channels and the pictrues look different in different color channels. For example, the "baboon.jpg" has very obivious color differences on the baboon's nose. The nose is nearly white in the red channel, while it shows black in green and blue channels.

    Y is luminance. Cb and Cr are blue and red color differences, repectly. As we can see, in Cr red goes darker while in Cb blue goes darker.

<img src="https://github.com/jhzhaofred/EC601_HW3/blob/master/images/Original.png" width = "270" height = "280" alt="Keyboard" align=center /> <img src="https://github.com/jhzhaofred/EC601_HW3/blob/master/images/Y.png" width = "270" height = "280" alt="Keyboard" align=center />

<img src="https://github.com/jhzhaofred/EC601_HW3/blob/master/images/cb.png" width = "270" height = "280" alt="Keyboard" align=center /> <img src="https://github.com/jhzhaofred/EC601_HW3/blob/master/images/cr.png" width = "270" height = "280" alt="Keyboard" align=center />

2. For values of pixel (20,25) at "baboon.jpg":

    R: 156 G: 165 B: 102 (Range: 0, 255)

    Y: 98 Cb: 129 Cr: 155 (Range: 0, 255)

    H: 165 S: 97 V: 34 (Range for H: 0, 360; Range for S, V: 0, 100)



# Referring
http://aishack.in/tutorials/opencvs-interface/
