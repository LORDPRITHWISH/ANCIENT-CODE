import cv2
import numpy as np
import tqdm
# Parameters for the video
zip_file_path = 'zippy\\test.zip'
output_video_filename = "video\\official_2x2.avi"


pix=8
# width, height = 1920, 1088
width, height = 3840 , 2160

with open(zip_file_path, 'rb') as zip_ref:
    binary_data = zip_ref.read() 
# print(len(binary_data))
# print(len(binary_data)*8/(1920*1088))

def create_binary_video(binary_data, output_video_filename, width, height):
    fourcc = cv2.VideoWriter_fourcc(*'HFYU')
    out = cv2.VideoWriter(output_video_filename, fourcc, 1, (width, height),False)

    frame = np.zeros((height, width), dtype=np.uint8)
    i=j=0
    for byte in tqdm.tqdm(binary_data):
        for bit_position in range(7, -1, -1):
            bit = (byte >> bit_position) & 1
            pixel_value = 255 if bit == 1 else 0            
            frame[i:i+pix,j:j+pix] = pixel_value
            j+=pix
            if j==width :
                j%=width
                i+=pix
                if i==height :
                    i%=height
                    out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
                    frame.fill(0)

    out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
    out.release()

create_binary_video(binary_data, output_video_filename, width, height)
