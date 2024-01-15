import cv2
import os

def images_to_video(image_folder, output_video):
    images = os.listdir(image_folder)  # Assuming the images are in alphabetical order
    print(*images,sep="\n")

# Usage example
image_folder = 'recognition\\output'  # Replace with the path to your folder containing images
output_video = 'recognition\\specimen\\generated_video.mp4'  # Replace with the desired output video filename

images_to_video(image_folder, output_video)
