import cv2
import os
import tqdm

def images_to_video(image_folder, output_video):
    images = os.listdir(image_folder)  # Assuming the images are in alphabetical order
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Choose the video codec (e.g., "mp4v", "XVID")
    # fps = 24  # Adjust the frames per second (fps) as desired
    fps = 10  # Adjust the frames per second (fps) as desired
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for image_name in tqdm.tqdm(images):
        image_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    video_writer.release()

# Usage example
image_folder = r'imjcompressor\shorted\4032_1860'  # Replace with the path to your folder containing images
output_video = 'imjcompressor\\trial\\take_2@10fps.mp4'  # Replace with the desired output video filename

images_to_video(image_folder, output_video)
