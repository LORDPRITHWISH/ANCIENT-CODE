import cv2
import math
import numpy as np

# Parameters for the video and decoding
video_filename = 'video\\official2_1x1.avi'
output_zip_filename = "resurected\\recovered_files.zip"
# threshold = 128  # Adjust this based on your encoding process

# Read video frames
cap = cv2.VideoCapture(video_filename)
binary_data = []
lframe=[]

def cut(fra,p=4):
    lis=[]
    temp=[]
    for row in fra :
        for pixel in row :
                if pixel[0]> 0 :
                    if temp:
                        lis.extend(temp)
                        temp.clear()
                    lis.append(pixel[0])
                else :
                    temp.append(pixel[0])
    return lis

def extract(fra):
    
    lis=[]
    for row in fra :
        for pixel in row :
            lis.append(pixel[0])         

    print('|',end='')
    return lis

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        # print([1 if pixel[0] > threshold else 0 for row in lframe for pixel in row])
        binary_data.extend(cut(lframe))
        break
    binary_data.extend(extract(lframe))
    lframe=frame.copy()

cap.release()

# Convert binary data to bytes

binary_bytes = bytearray()
# for i in range(0, len(binary_data), 8):
#     byte = 0
#     for j in range(8):
#         byte |= (binary_data[i + j] << (7 - j))
# binary_bytes.extend( byte for byte in binary_data)

# Save as ZIP file-+
with open(output_zip_filename, "wb") as zip_file:
    zip_file.write(binary_bytes)

# import compare
# compare.compare()
