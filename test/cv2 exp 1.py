import cv2

imj=cv2.imread(r'test\test2.png',-1)
cv2.imshow('RONIE',imj)
cv2.waitKey(0)
# imj.view()
# imj=cv2.blur(imj,(10,10))
cv2.blur(imj,(2,1),imj,(0,0),cv2.BORDER_REFLECT)
cv2.erode(imj,(10000000,1000),imj,(0,0),cv2.BORDER_REFLECT)
# cv2.blur(imj,(2,2),imj,(0,0),cv2.BORDER_REFLECT)


# cv2.borderInterpolate(50,50,cv2.BORDER_DEFAULT)
# cv2.scaleAdd()
cv2.imshow('RONIE',imj)
cv2.waitKey(0)