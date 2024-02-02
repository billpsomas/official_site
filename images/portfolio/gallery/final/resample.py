import cv2
import os
from PIL import Image

size = 6016,4000

input_dir = 'C://Users//Bill//Desktop//Ceevee_2_0_0//images//portfolio//gallery'
output_dir = os.getcwd()

for i in range(len(os.listdir(input_dir))):
	print('Reading -> ' + str(os.listdir(input_dir)[i]))
	im = Image.open(input_dir + '//' + os.listdir(input_dir)[i])
	im.thumbnail(size, Image.ANTIALIAS)
	im.save(output_dir + '//' + str(i) + '.jpg', "JPEG")
