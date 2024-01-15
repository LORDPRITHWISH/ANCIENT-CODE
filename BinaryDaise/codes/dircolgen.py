import cv2
import numpy as np
import tqdm
import os
# Parameters for the video
# output_video_filename = "video\\binary_video_1f1-500.avi"

out='quality\\dirimj {}'
width, height = 6400, 3900
# width, height = 500, 500
name='direct-pro '
i=0
while os.path.exists(out.format(i)):
    i+=1
out=out.format(i)
os.mkdir(out)

# Read the binary data  
with open("zippy\\output.zip", "rb") as binary_file:
    binary_data = binary_file.read()

# Function to create video from binary data
def create_binary_video(binary_data, width, height):

    frame = np.zeros((height, width,3), dtype=np.uint8)
    i=j=k=num=0
    for byte in tqdm.tqdm(binary_data):
            frame[i,j,k] = byte
            k+=1
            if k==3 :
                k%=3
                j+=1
                if j==width :
                    j%=width
                    i+=1
                    if i==height :
                        i%=height
                        cv2.imwrite(f"{out}//{name}{num:05d}.png",frame)
                        num+=1
                        frame.fill(0)
             
    cv2.imwrite(f"{out}//{name}{num:05d}.png",frame)

# Create the binary video
create_binary_video(binary_data,width, height)
