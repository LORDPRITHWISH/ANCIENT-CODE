import cv2
import os 
op="recognition\\output"
i=0
while True:
    if not(os.path.exists(f"{op}//shot{i}.jpg")):
        print("tata")
        break
    img =cv2.imread(f"{op}//shot{i}.jpg")
    cv2.imshow("WTF",img)
    key=cv2.waitKey()
    i+=1
    if key== ord("q"):
        break

cv2.destroyAllWindows()