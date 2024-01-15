from moviepy.editor import *
import os
inp=r"d:\YOUTUBE\bulk"
out=r"D:\YOUTUBE\COMBINATION"
files=os.listdir(inp)
# print(files)
for i in files :    
    if i.endswith(".mp4") :
        n=i[0:-10]
    elif i.endswith(".webm") :
        n=i[0:-11]
    else :
        continue
    # print(n)
    aud=os.path.join(inp,i)
    vid=os.path.join(inp,n)
    print(vid)
    if os.path.exists(vid) :
        print("good")
        vicl=VideoFileClip(vid)
        aucl=AudioFileClip(aud)
        
        viau=vicl.set_audio(aucl)
        des=os.path.join(out,i)
        viau.write_videofile(des)
        print("done-pri")
        os.remove(aud)
        os.remove(vid)
        print("REMONED","\n"*20)