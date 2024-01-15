# import cv2
import numpy as np
# import tqdm
import pandas as pd
# Parameters for the video
output_video_filename = "video\\col_video_2f1.avi"
pix=20 
# width, height = 1920, 1088  
# width, height = 1920, 1080  
# width, height = 500, 500

# Read the binary data  
# with open("output\\data.bin", "rb") as binary_file:
#     binary_data = binary_file.read()
with open("output\\combined_binary.bin", "rb") as binary_file:
    binary_data = binary_file.read()

# Function to create video from binary data
def create_binary_video(binary_data):
    
    find=255
    
    # bibi=list(map(lambda bi: np.uint8(bi), binary_data))
    # del(binary_data)
    ze=[0]*100000
    # for i in range(bibi) :
    #     if bibi[i]==0 :
    i=0
    while(i<len(binary_data)) :
        if binary_data[i]==find :
            count = 0
            try :
                while binary_data[i]==find :
                    count+=1
                    i+=1
            except Exception as e:
                print (e)
            ze[count]+=1
        i+=1
            
    for i,j in enumerate(ze) :
        if j>0 :
            print(f"{i} :- {j}")   
        
    # counted=dict(pd.Series(bibi).value_counts())
    # print(counted.get(0))
    # for i in counted:
    #     print(f'{i}-> {counted.get(i)}')
    

# Create the binary video
create_binary_video(binary_data)
