import cv2
import math

# Parameters for the video and decoding
video_filename = 'video\\official0_1x1.avi'
output_zip_filename = "resurected\\recovered_files.zip"
threshold = 128  # Adjust this based on your encoding process

# Read video frames
cap = cv2.VideoCapture(video_filename)
binary_data = []
lframe=[]

def cut(fra,p=4):
    lis=[]
    temp=[]
    te=f=0
    for row in fra :
        for pixel in row :
            if f==p-1:
                te+=pixel[0]//p
                if te> threshold :
                    if temp:
                        lis.extend(temp)
                        temp.clear()
                    lis.append(1)
                else :
                    temp.append(0)
                te=f=0
            else :
                te+=pixel[0]//p
                f+=1           
    x=len(lis)
    # print(x)
    if x < 8 :
        r=8-x
    else:
        r=(math.ceil(x/8)*8)-x
        
    for _ in range(r):
        lis.append(0)
    print('\n',x,len(lis))
    return lis

def extract(fra,p=4):
    
    lis=[]
    temp=f=0
    # [1 if pixel[0] > threshold else 0 for row in frame for pixel in row]
    for row in fra :
        for pixel in row :
            if f==p-1:
                temp+=pixel[0]//p
                lis.append(1 if temp > threshold else 0)
                temp=f=0
            else :
                temp+=pixel[0]//p
                f+=1
    print('|',end='')
    return lis

pix=1
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        # print([1 if pixel[0] > threshold else 0 for row in lframe for pixel in row])
        binary_data.extend(cut(lframe,pix))
        break
    binary_data.extend(extract(lframe,pix))
    lframe=frame.copy()

cap.release()

# Convert binary data to bytes

binary_bytes = bytearray()
for i in range(0, len(binary_data), 8):
    byte = 0
    for j in range(8):
        byte |= (binary_data[i + j] << (7 - j))
    binary_bytes.append(byte)

# Save as ZIP file-+
with open(output_zip_filename, "wb") as zip_file:
    zip_file.write(binary_bytes)

# import compare
# compare.compare()
