import cv2
# pa="video\\binary_video_2f1.avi"
pa="video\\official_1x1.avi"
# pa=r"imjcompressor\sample\truth.mp4"
op="image"
def splitter(path,output,name="PIC-"):
    cap = cv2.VideoCapture(path)
    i=0
    ret=1
    print("started")
    while ret:
        ret,frame=cap.read()
        if ret :
            cv2.imwrite(f"{output}//{name}{i:05d}.png",frame)
            i+=1
        # print(ret)
    cv2.destroyAllWindows()
    
splitter(pa,op,"truth_broken")