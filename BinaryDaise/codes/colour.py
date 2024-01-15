import cv2
import numpy as np
# import tqdm
# Parameters for the video
output_video_filename = "video\\coloursori.avi"
# pix=20 
# width, height = 1920, 1088  
width, height = 1920, 1080  
# width, height = 500, 500

# Function to create video from binary data
def create_binary_video(width, height):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_filename, fourcc, 1, (width, height))

    # i=j=0
    for i in range(255):     
        frame =i* np.ones((height, width), dtype=np.uint8)

        # out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
        out.write(frame)
        # cv2.imshow("feed", cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
        cv2.imshow("feed", cv2.cvtColor(frame, cv2.COLOR_rgb))
        cv2.imshow("feed", frame)
        key=cv2.waitKey(1)
        if key== ord("q") or key== ord("Q"):
            break
        # frame[:,:] = 0
    out.release()
    cv2.destroyAllWindows()

# Create the binary video
create_binary_video(width, height)
