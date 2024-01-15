import cv2
import os
import tqdm
import shutil

inp="imjcompressor\\images"
out="imjcompressor\\shorted"

# fol=os.listdir(out)
# li=[]

# for i in fol :
#     x=[int(j) for j in i.split()]

#     for i in li :
#         if i[0]==x[0] :
#             i[1].append(x[2])
#             break
#     else :
#         li.append([x[0,[x[1]]]])



imj=os.listdir(inp)
for i in range(3):
    tar=os.path.join(inp,imj[i])
    frame = cv2.imread(tar)
    h,w,_=frame.shape
    
    # for j in li :
    #     if k[0]==h :
    #         for k in j[1] :
    #             sopo=f"{out}//{j} {k}"
    #             shutil.move(tar,sopo)
    
    sopo=f"{out}\\{w}_{h}"
    if not os.path.exists(sopo):
        os.mkdir(sopo)
    shutil.move(tar,sopo)
    
