import cv2
import numpy as np
import tqdm
# Parameters for the video
output_video_filename = "video\\binary_video_2f1.avi"
pix=2 
width, height = 1920, 1088
# width, height = 500, 500

# Read the binary data  
with open("output\\data.bin", "rb") as binary_file:
    binary_data = binary_file.read()

# Function to create video from binary data
def create_binary_video(binary_data, output_video_filename, width, height):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_filename, fourcc, 1, (width, height))

    frame = np.zeros((height, width), dtype=np.uint8)
    i=j=0
    # for byte in binary_data:
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
                    # out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
                    out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
                    # cv2.imshow("feed", cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
                    # key=cv2.waitKey(1)
                    # if key== ord("q") or key== ord("Q"):
                    #     break
                    frame[:,:] = 0
            # print(bit)
        # print(byte)
        # print('\n'*10)
    out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
    out.release()
    # cv2.destroyAllWindows()

# Create the binary video
create_binary_video(binary_data, output_video_filename, width, height)
