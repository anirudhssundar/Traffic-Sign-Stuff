import numpy as np
import cv2
import os
import shutil

thirty_cascade = cv2.CascadeClassifier('30_cascade-10stages.xml')

#yield_cascade = cv2.CascadeClassifier('yieldsign12Stages.xml')

#speed_cascade = cv2.CascadeClassifier('/home/anirudh/Documents/haar_xml_files/haarCascade_speed.xml')

path = "/home/anirudh/Documents/Real_test/workspace-30/Test/"
newpath = "/home/anirudh/Documents/Real_test/workspace-30/there3/"

path_20 = "/home/anirudh/Documents/Real_test/workspace2/pos/"

#img = cv2.imread('12614.ppm',1)

dirs = sorted(os.listdir(newpath))
for image in dirs:
	#print(dirs)

	#img = cv2.imread('12614.ppm',1)
	img = cv2.imread(newpath + image,1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


	n = np.arange(1.1,2,0.1)
	#print(n)

	thirties = thirty_cascade.detectMultiScale(gray,1.2,1)
	for(x,y,w,h) in thirties:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		#cv2.imshow('img',img)
		#cv2.waitKey(0)
	if thirties == ():
		print("n")
		#shutil.move(path +image,"/home/anirudh/Documents/Real_test/workspace2/nope/"+ image)
	else:
		shutil.move(newpath +image,"/home/anirudh/Documents/Real_test/workspace-30/there2/"+ image)
		#print("img = cv2.imread('12614.ppm',1)y")
		#cv2.imshow('img',img)
		#cv2.waitKey(0)
'''

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