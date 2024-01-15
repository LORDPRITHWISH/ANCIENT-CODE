import cv2
import numpy as np
import tqdm
import os
import shutil
# Parameters for the video
zip_file_path = 'zippy\\test.zip'
output_video_filename = "video\\official{}_{}.avi"
output_image="image\\trial-{}"

class zipper :
    
    def __init__(self,ov=output_video_filename,ij=output_image,pi=1,pj=4) -> None:        
        self.pixi=pi
        self.pixj=pj
        if pj==1:
            self.width, self.height = 1920 , 1080
        if pj==4:
            self.width, self.height = 1088, 650
        if pj==3:
            self.width, self.height = 1152, 650
        if pj==10:
            self.width,self.height=6400 , 3900
        self.output_video=ov
        self.image=ij

    def runner(self):
        # global output_video_filename,self.image
        i=0
        if os.path.exists(zip_file_path) :
            while os.path.exists(self.output_video.format(i,f"{self.pixi}x{self.pixj}")):
                i+=1
            self.output_video= self.output_video.format(i,f"{self.pixi}x{self.pixj}")
            self.image=self.image.format(f"{self.pixi}x{self.pixj}-{i}")
            if os.path.exists(self.image):
                shutil.rmtree(self.image)
            os.makedirs(self.image)
            self.unzip()
            self.splitter(self.output_video,self.image,"truth")
        
            
    
    def unzip(self) :
        with open(zip_file_path, 'rb') as zip_ref:
            binary_data = zip_ref.read() 
            self.create_binary_video(binary_data)


    def create_binary_video(self,binary_data):
        fourcc = cv2.VideoWriter_fourcc(*'HFYU')
        out = cv2.VideoWriter(self.output_video, fourcc, 1, (self.width, self.height))

        frame = np.zeros((self.height, self.width), dtype=np.uint8)
        i=j=0
        for byte in tqdm.tqdm(binary_data):         
                frame[i:i+self.pixi,j:j+self.pixj] = byte
                j+=self.pixj
                if j==self.width :
                    j%=self.width
                    i+=self.pixi
                    if i==self.height :
                        i%=self.height
                        out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
                        frame.fill(0)
                        # print('\n'*10)

        out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
        out.release()
        print(self.output_video)

    def splitter(self,path,output,name="PIC-"):
        cap = cv2.VideoCapture(path)
        i=0
        ret=1
        print("started")
        while ret:
            ret,frame=cap.read()
            if ret :
                cv2.imwrite(f"{output}//{name}{i:05d}.png",frame)
                i+=1
        print("DONE WITH", os.path.split(output)[1])
            
        # cv2.destroyAllWindows()
    
cre=zipper(pj=1)
cre.runner()

    
# splitter(pa,op,"truth_broken")
