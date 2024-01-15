import cv2
Reference_img =cv2.imread("C:\\Users\\PRITHWISH\\Desktop\\CODE\\recognition\\Camera\\iron.jpg")

cv2.imshow("feed", Reference_img)


while True:
    key=cv2.waitKey(10)
    if key== ord("q"):
        break

cv2.destroyAllWindows()