import os
import cv2
import os 
import numpy as np

path="Teat"
i=0

per=os.listdir(path)
for i in per:
    pepa=os.path.join(path,i)
    pic=os.listdir(pepa)
    for j in pic:
        out=os.path.join(pepa,j)
        img =cv2.imread(out)
        cv2.imshow("feed",img)
        key=cv2.waitKey(1)
        if key== ord("q"):
            break
    else:
        continue
    break

cv2.destroyAllWindows() 
