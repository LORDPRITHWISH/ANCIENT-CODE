import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 490)
i=0
while True:

    ret, frame=cap.read()
    cv2.imwrite(f"recognition\\taken\\pic{i}.jpg",frame)
    
    cv2.putText(frame,f"{i}", (20, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 3)
    cv2.imshow("feed", frame)
    i+=1
    key=cv2.waitKey(25)
    if key== ord("q"):
        break

cv2.destroyAllWindows()