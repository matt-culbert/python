from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import os
import send_mail
import re
from ml import calculate

def mean_squared_error(image1, image2):
	list_of_files = glob.glob('/home/pi/Desktop/camera/*.jpg')
	latest_file = max(list_of_files, key=os.path.getctime) # get latest file in our directory

	text = "Possible motion detected"
	subject = "Pi security camera alert"
	send_to = "matthew.culbert@mymail.champlain.edu"
	send_from = "dicek6@gmail.com"

	#Load images
	original = cv2.imread("control.jpg", 0) # control file of what the house looks like
	questionable = cv2.imread(latest_file, 0)
		
	image1 = image1.astype(float)
	image2 = image2.astype(float)
	error_rank = np.sum((image1 - image2) ** 2)
	error_rank /= float(image1.shape[0] * image1.shape[1])
	test = calculated(error_ranking)
	if test == True:
		send_mail(send_from, send_to, subject, text, latest_file)
	else: 
		time1 = time.strftime("%d/%m/%Y %H:%M:%S")
		re.sub('[^A-Za-z0-9]+', '', time1)
		f = open(error_rank+"-"time1+".txt", 'w+')
		f.close

if __name__ == '__main__':
	error_ranking = mean_squared_error(original, questionable)

# add MSE to the name of the file, before the date
# learn average MSE over time
# use this to set a more accurate threshold to alert on
# use time of day based learning to pick up habits
# write MSE to a file to reference seperately over time? since images get deleted after x time
# example --> 123-1_2_18-242354352 --> seperate on first hyphen --> 