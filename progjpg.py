import os
from PIL import Image, ImageFile

def convert_jpg(img_dir, scale_img, img_quality):
	img_file = Image.open(img_dir)
	if(scale_img == 100):
		width, height = img_file.size
	else:
		width, height = (int(scale_img * img_file.size[0] / 100.0), int(scale_img * img_file.size[1] / 100.0))

	img_File = img_file.resize((width,height),Image.ANTIALIAS)

	try:
		img_file.save(img_dir, optimize=True, quality=img_quality, progressive=True)
	except IOError:
		ImageFile.MAXBLOCK = width * height
		img_file.save(img_dir, optimize=True, quality=img_quality, progressive=True)
