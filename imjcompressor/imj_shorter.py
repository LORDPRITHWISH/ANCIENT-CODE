import cv2
import os
import shutil

inp="imjcompressor\\images"
out="imjcompressor\\shorted"

imj=os.listdir(inp)
for i in range(3):
    
    tar=os.path.join(inp,imj[i])
    frame = cv2.imread(tar)
    h,w,_=frame.shape
    
    sopo=f"{out}\\{w}_{h}"
    
    if not os.path.exists(sopo):
        os.mkdir(sopo)
        
    shutil.move(tar,sopo)
    
