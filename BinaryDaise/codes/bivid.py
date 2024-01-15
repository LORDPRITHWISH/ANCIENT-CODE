import cv2
import numpy as np
import tqdm

# Parameters for the video
output_video_filename = "video\\binary_video.avi"
width, height = 640, 480
frame_duration_ms = 100  # Adjust as needed

# Read the binary data
with open("output\\combined_binary.bin", "rb") as binary_file:
    binary_data = binary_file.read()

# Function to create video from binary data
def create_binary_video(binary_data, output_video_filename, width, height, frame_duration_ms):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_filename, fourcc, 10, (width, height), False)

    for byte in tqdm.tqdm(binary_data):
        for bit_position in range(7, -1, -1):
            bit = (byte >> bit_position) & 1
            pixel_value = 255 if bit == 1 else 0
            frame = (pixel_value * np.ones((height, width), dtype=np.uint8))
            out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
            cv2.waitKey(frame_duration_ms)

    out.release()
    cv2.destroyAllWindows()

# Create the binary video
create_binary_video(binary_data, output_video_filename, width, height, frame_duration_ms)
