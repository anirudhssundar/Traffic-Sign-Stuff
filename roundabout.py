import numpy as np
import cv2
import os

#paths to positive and negative images
path1 = "/home/anirudh/Documents/Real_test/Workspace/neg/"
path2 = "/home/anirudh/Documents/Real_test/Workspace/pos/"
dirs = os.listdir( path2 )  #change to path1 when using negative



#function to resize images
def resize():
	for item in dirs:
		if os.path.isfile(path+item):
			img = cv2.imread(path+item)
			#f, e = os.path.splitext(path+item)
			res = cv2.resize(img, (100,100))
			cv2.imwrite(path+item,res)

			
def create_pos_neg():
	for file_type in [path2]:
		for img in os.listdir(file_type):
			
			
			if file_type == path2:
				line = file_type+img+' 1 0 0 50 50 \n' # start x and y coordinate end x and y coordinate
				with open('info.dat','a')  as f:   #creates a .dat file with the image path and coordinates
					f.write(line)
			
			elif file_type == path1:
				line = file_type+img+'\n'
				with open('bg.txt','a') as f:   #bg.txt contains path to negative images
					f.write(line)

#used to increase the number of positive images
#appends one positive image on  100 negative images to give 100 positive samples
def create_samples():
	f = open("info/info.lst","a")
	for file_type in [path2]:
		for image in os.listdir(file_type):
			os.system("opencv_createsamples -img /home/anirudh/Documents/Real_test/Workspace/pos/"+image+" -bg bg.txt -info info/info1.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 100")
			r = open("info/info1.lst","r")
			f.write(r.read())
			r.close()
	f.close()
			


create_samples()
#create_pos_neg()			
#resize()
