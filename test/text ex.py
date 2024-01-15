import pytesseract
import cv2
import PIL.Image



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# loc='test\\test.png'
loc=r'C:\Users\prithis\Desktop\py storage\pic to text\specimen.jpg'

con='--psm 11'


print(pytesseract.image_to_string(PIL.Image.open(loc),config=con))

imj=cv2.imread(loc)
# print(imj.shape)
hi,wi,_= imj.shape
# boxes=pytesseract.image_to_boxes(imj,config=con)
boxes=pytesseract.image_to_data(imj,config=con,output_type=pytesseract.Output.DICT)

# print(boxes.splitlines())
# print(boxes)

# for i in boxes.splitlines() :
#     i=i.split()
#     # cv2.rectangle(imj,(int(i[1]),int(i[2])),(int(i[3]),int(i[4])),(255,0,0),5)
#     cv2.rectangle(imj,(int(i[1]),hi-int(i[2])),(int(i[3]),hi-int(i[4])),(255,0,0),1)

# print(len(boxes))
# print(len(boxes['conf']))
for i in range(len(boxes['conf'])) :
    if boxes['conf'][i] > 0 :
        x,y,w,h=boxes['left'][i],boxes['top'][i],boxes['width'][i],boxes['height'][i]
        cv2.rectangle(imj,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(imj,boxes['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,200,100),2,cv2.LINE_AA)



cv2.imshow('imj',imj)
cv2.waitKey(0)
    