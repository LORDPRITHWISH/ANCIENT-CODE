import cv2

# Parameters for the video and decoding
video_filename = 'video\\official_0.avi'
output_zip_filename = "resurected\\recovered_files.zip"
# threshold = 128  # Adjust this based on your encoding process

# Read video frames
binary_data = []
lframe=[]

def cut(fra,p=4):
    lis=[]
    temp=[]
    for row in fra :
        for pixel in row :
            for byte in pixel :
                if byte> 0 :
                    if temp:
                        lis.extend(temp)
                        temp.clear()
                    lis.append(byte)
                else :
                    temp.append(byte)
    print('done')
    return lis

def extract(fra):
    
    lis=[]
    for row in fra :
        for pixel in row :
            for byte in pixel :
                lis.append(byte)         

    print('|',end='')
    return lis

cap = cv2.VideoCapture(video_filename)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        binary_data.extend(cut(lframe))
        break
    binary_data.extend(extract(lframe))
    lframe=frame
cap.release()
print('oki')
# Convert binary data to bytes
binary_bytes = bytearray()
binary_bytes.extend(binary_data)
print("con")
del(binary_data)
with open(output_zip_filename, "wb") as zip_file:
    zip_file.write(binary_bytes)

