import cv2

imj=cv2.imread(r'test\test2.png',-1)
i=0
while 1 :
    i+=1
    cv2.blur(imj,(2*i,1),imj,(0,0),cv2.BORDER_REFLECT)
    cv2.erode(imj,(1,1),imj,(0,0),cv2.BORDER_REFLECT)
    # cv2.blur(imj,(2,2),imj,(0,0),cv2.BORDER_REFLECT)
    print(i)
    cv2.imshow('RONIE',imj)
    cv2.waitKey(10)