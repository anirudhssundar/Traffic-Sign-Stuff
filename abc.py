import numpy as np
import cv2
import os

path = "/home/anirudh/Documents/Haar_time/opencv_workspace/negative_images"
dirs = os.listdir( path )


#resizing function
def resize():
	for item in dirs:
		if os.path.isfile(path+item):
			img = cv2.imread(path+item)
			#f, e = os.path.splitext(path+item)
			res = cv2.resize(img, (50,50))
			cv2.imwrite(path+item,res)

			
#creates the bg.txt and the info.dat files 
def create_neg():
	for file_type in [path]:
		for img in os.listdir(file_type):
			
			if file_type == path:
				line = file_type+'/'+img+'\n'
				with open('bg.txt','a') as f:
					f.write(line)
'''
def samples():
	for file_type in [path]:
		for img in os.listdir(file_type):
			opencv_createsamples -img -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 800
'''
#samples()			
create_neg()
			

			
			
#resize()