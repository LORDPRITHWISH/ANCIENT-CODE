import cv2
import os 
i=0
while True:
    if not(os.path.exists(f"recognition\\taken\\pic{i}.jpg")):
        # i=0
        break
    img =cv2.imread( f"recognition\\taken\\pic{i}.jpg")
    cv2.imshow("feed",img)
    key=cv2.waitKey(1)
    i+=1
    if key== ord("q"):
        break

cv2.destroyAllWindows()