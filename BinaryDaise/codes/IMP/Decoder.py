import cv2

# Parameters for the video and decoding
video_filename = 'video\\official_1.avi'
output_zip_filename = "resurected\\recovered_files.zip"
# threshold = 128  # Adjust this based on your encoding process

lframe=[]

def cut(fra,p=4):
    lis=[]
    temp=[]
    for row in fra :
        for pixel in row :
            for byte in pixel :
                if byte==255 :
                    if temp:
                        lis.extend(temp)
                        temp.clear()
                    temp.append(byte)
                elif byte> 0 :
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


binary_bytes = bytearray()
with open(output_zip_filename, "wb") as zip_file:
    zip_file.write(binary_bytes)
    
cap = cv2.VideoCapture(video_filename)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        binary_bytes.extend(cut(lframe))
        with open(output_zip_filename, "ab") as zip_file:
            zip_file.write(binary_bytes)
        binary_bytes.clear()
        break
    
    binary_bytes.extend(extract(lframe))
    with open(output_zip_filename, "ab") as zip_file:
        zip_file.write(binary_bytes)
    binary_bytes.clear()
    lframe=frame
    
cap.release()
print('oki')