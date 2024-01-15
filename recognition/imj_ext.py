import cv2
pa="recognition\\specimen\\specimen.mp4"
op="recognition\\output"
def splitter(path,output,name):
    cap = cv2.VideoCapture(path)
    i=0
    ret=1
    while ret:

        ret,frame=cap.read()
        cv2.imwrite(f"{output}//{name}{i:05d}.jpg",frame)
        i+=1
    cv2.destroyAllWindows()
    
splitter(pa,op,"trial")