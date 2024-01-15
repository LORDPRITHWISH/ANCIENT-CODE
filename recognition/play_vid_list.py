import cv2
import os 
import numpy as np
import tqdm
pat="recognition\\output"
i=0
arr=[]
per=os.listdir(pat)


for i in tqdm.tqdm(per[::4]):
    out=os.path.join(pat,i)
    arr.append(cv2.imread(out))
print("STARTING CONVERTION")    
img = np.array(arr)
del(arr)
i=0
l=len(img)
print("READY -->")
while True:
    if i>=l:
        i=0
        # break
    cv2.imshow("MADNESS",img[i])
    key=cv2.waitKey(1)
    i+=1
    if key== ord("q"):
        break

cv2.destroyAllWindows()
