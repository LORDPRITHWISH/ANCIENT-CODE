import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 490)

while True:

    ret, frame=cap.read()

    cv2.imshow("feed", frame)
    

    key=cv2.waitKey(10)
    if key== ord("q"):
        break

cv2.destroyAllWindows()