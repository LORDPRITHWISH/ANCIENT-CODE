import cv2
import numpy as np
import tqdm
# Parameters for the video
# output_video_filename = "video\\binary_video_1f1-500.avi"

out=r'video\dirimj'
pix=1
width, height = 1920, 1080
# width, height = 500, 500
name='direct-pro.2-b'

# Read the binary data  
with open("zippy\\test.zip", "rb") as binary_file:
    binary_data = binary_file.read()

# Function to create video from binary data
def create_binary_video(binary_data, width, height):

    frame = np.zeros((height, width,3), dtype=np.uint8)
    # frame = np.asarray((height, width), dtype=[0,0,0])
    
    i=j=k=0
    # for byte in binary_data:
    for byte in tqdm.tqdm(binary_data):
        for bit_position in range(7, -1, -1):
            bit = (byte >> bit_position) & 1
            pixel_value = 255 if bit == 1 else 0            
            frame[i:i+pix,j:j+pix,:] = pixel_value
            j+=pix
            if j==width :
                j%=width
                i+=pix
                if i==height :
                    i%=height
                    # out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
                    # out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
                    cv2.imwrite(f"{out}//{name}{k:05d}.png",frame)
                    k+=1

                    frame.fill(0)
    while(i<height):
        while(j<width):
            frame[i:i+pix,j:j+pix,2:2] = 255
            j+=1
        i+=1
    k+=1                    
    cv2.imwrite(f"{out}//{name}{k:05d}.png",frame)

# Create the binary video
create_binary_video(binary_data,width, height)
