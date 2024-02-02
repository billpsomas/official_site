import cv2
import os
from PIL import Image

size = 1200,800

input_dir = 'C://Users//Bill//Desktop//Ceevee_2_0_0//images//portfolio//gallery'
output_dir = os.getcwd()

for i in range(len(os.listdir(input_dir))):
	print('Reading -> ' + str(os.listdir(input_dir)[i]))
	images = os.listdir(input_dir)
	im = Image.open(input_dir + '//' + images[i])
	im.thumbnail(size, Image.ANTIALIAS)
	im.save(output_dir + '//' + images[i], "JPEG")
