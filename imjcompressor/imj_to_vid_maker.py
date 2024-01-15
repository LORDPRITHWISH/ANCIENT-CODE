import cv2
import os
import tqdm
import shutil

inp="imjcompressor\\JPG"
out="imjcompressor\\shorted"
viout="imjcompressor\\movie"

def shorter():
    imj=os.listdir(inp)
    for i in tqdm.tqdm(imj):
        
        tar=os.path.join(inp,i)
        frame = cv2.imread(tar)
        h,w,_=frame.shape
        
        sopo=f"{out}\\{w}_{h}"
        
        if not os.path.exists(sopo):
            os.mkdir(sopo)
            
        shutil.move(tar,sopo)
        
        
def movie_maker(imjfol):
    images = os.listdir(imjfol)
    frame = cv2.imread(os.path.join(imjfol, images[0]))
    height, width, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 24 
    out=f"{viout}//colage{width}_{height}@PRITHWISH.mp4"
    video_writer = cv2.VideoWriter(out, fourcc, fps, (width, height))

    for image_name in tqdm.tqdm(images):
        image_path = os.path.join(imjfol, image_name)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    video_writer.release()
    
def vid_driver():
    folders=os.listdir(out)
    for i in folders :
        print("THE CURRENT FOLDER IS :  ",i)
        fol=os.path.join(out,i)
        movie_maker(fol)
        
shorter()
vid_driver()