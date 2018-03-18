import numpy as np
import cv2
import os
import shutil

#Create a folder 'There' for storing images in which the sign is detected


#The Classifier file

thirty_cascade = cv2.CascadeClassifier('30_cascade-10stages.xml')

#yield_cascade = cv2.CascadeClassifier('yieldsign12Stages.xml')

#speed_cascade = cv2.CascadeClassifier('/home/anirudh/Documents/haar_xml_files/haarCascade_speed.xml')

#Path to the test dataset

path = "/home/anirudh/Documents/Real_test/workspace-30/Test/"


# Testing the data on a folder of images
dirs = sorted(os.listdir(path))
for image in dirs:
	#print(dirs)
	img = cv2.imread(path + image,1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	#change the parameters 1.2 and 1 depending on the situation
	thirties = thirty_cascade.detectMultiScale(gray,1.2,1)
	for(x,y,w,h) in thirties:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		
	if thirties == ():
		print("n")
		#shutil.move(path +image,"/home/anirudh/Documents/Real_test/workspace2/nope/"+ image)
	else:
		shutil.move(path +image,"/home/anirudh/Documents/Real_test/workspace-30/there/"+ image)
		#print("img = cv2.imread('12614.ppm',1)y")
		#cv2.imshow('img',img)
		#cv2.waitKey(0)
'''
#Code for checking if the Cascade works on just one image

img = cv2.imread('00224.ppm',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#res = cv2.resize(gray,(60,60))
twenties = twenty_cascade.detectMultiScale(gray,2,1)
for(x,y,w,h) in twenties:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		
cv2.imshow('i',img)
cv2.waitKey(0)
'''
		
		
cv2.destroyAllWindows()
