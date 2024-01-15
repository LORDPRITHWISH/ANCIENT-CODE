import cv2
pa="imjcompressor\\trial\\take_1@15fps.mp4"
# pa=r"imjcompressor\sample\truth.mp4"
op="imjcompressor\\output"
def splitter(path,output,name="PIC-"):
    cap = cv2.VideoCapture(path)
    i=0
    ret=1
    print("started")
    while ret:
        ret,frame=cap.read()
        if ret :
            cv2.imwrite(f"{output}//{name}{i:05d}.jpg",frame)
            i+=1
        # print(ret)
    cv2.destroyAllWindows()
    
splitter(pa,op,"truth_broken")