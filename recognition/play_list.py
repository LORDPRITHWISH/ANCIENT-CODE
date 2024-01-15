import cv2
import os 
import numpy as np
i=0
arr=[]
while os.path.exists(f"recognition\\taken\\pic{i}.jpg"):
    arr.append(cv2.imread( f"recognition\\taken\\pic{i}.jpg"))
    i+=1
img = np.array(arr)
i=0
l=len(img)
while True:
    if i>=l:
        # i=0
        break
    # img =cv2.imread( f"recognition\\taken\\pic{i}.jpg")
    cv2.imshow("feed",img[i])
    key=cv2.waitKey(1)
    i+=1
    if key== ord("q"):
        break

cv2.destroyAllWindows()