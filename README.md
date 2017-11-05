# EC601_HW3
# Exercise 1
How does a program read the cvMat object, in particular, what is the order of the pixel structure?

A: Normally, the cvMat object will be read by using cvMatName.at(x,y). Starting from the Top-left, the matrix is orgnized in the following order:

![alt text](http://aishack.in/static/img/tut/cpp-mat.jpg)

If there are more than one elements in one entry, such as RGB channels, then the sub-elements will be accessed by using cvMatName.at(x,y)[index].

# Exercise 2



# Referring
http://aishack.in/tutorials/opencvs-interface/
