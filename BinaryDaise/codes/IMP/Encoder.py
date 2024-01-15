import cv2
import numpy as np
import tqdm
import os
import shutil
# Parameters for the video
zip_file_path = 'zippy\\output.zip'
output_video_filename = "video\\official_{}.avi"
output_image="image\\trial-{}"

class zipper :
    
    def __init__(self,ov=output_video_filename,ij=output_image) -> None:        
        self.width, self.height = 10 , 10
        self.output_video=ov
        self.image=ij

    def runner(self):
        i=0
        if os.path.exists(zip_file_path) :
            while os.path.exists(self.output_video.format(i)):
                i+=1
            self.output_video= self.output_video.format(i)
            self.image=self.image.format(i)
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
        frame = np.zeros((self.height, self.width,3), dtype=np.uint8)
        i=j=k=0
        for byte in tqdm.tqdm(binary_data):
                frame[i,j,k] = byte
                k+=1
                if k==3 :
                    k%=3
                    j+=1
                    if j==self.width :
                        j%=self.width
                        i+=1
                        if i==self.height :
                            i%=self.height
                            out.write(frame)
                            frame.fill(0)
        frame[i,j,k] = 255
        out.write(frame)
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
    
cre=zipper()
cre.runner()

    
# splitter(pa,op,"truth_broken")
