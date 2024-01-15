import os
import cv2
from PIL import Image
print(os.getcwd())
# os.chdir("C:\\Python\\Geekfolder2")
path = "recognition\\output"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir(path))

for file in os.listdir(path):
	im = Image.open(os.path.join(path, file))
	width, height = im.size
	mean_width += width
	mean_height += height

mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

for file in os.listdir(path):
	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
		# opening image using PIL Image
		im = Image.open(os.path.join(path, file))

		# im.size includes the height and width of image
		width, height = im.size
		print(width, height)

		# resizing
		imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
		imResize.save( file, 'JPEG', quality = 95) # setting quality
		# printing each resized image name
		print(im.filename.split('\\')[-1], " is resized")


def generate_video():
	image_folder = path # make sure to use your folder
	video_name = 'mygeneratedvideo.mp4'
	# os.chdir("recognition\\specimen")
	
	images = [img for img in os.listdir(image_folder)
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")]
	
	print(images)

	frame = cv2.imread(os.path.join(image_folder, images[0]))

	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, 0, 1, (width, height))

	for image in images:
		video.write(cv2.imread(os.path.join("recognition\\specimen", image)))
	
	cv2.destroyAllWindows()
	video.release() # releasing the video generated


generate_video()
