from tkinter import *
#import random
from time import *
import time

w=Tk()
# w.geometry("1600x1000")
w.geometry("1000x400")
t = time.localtime(time.time())
# localtime = time.asctime(t)
# str = "Current Time:" + time.asctime(t)
l=Label(w,text='',font=("Goudy Stout",30))
l.pack(side="top",padx=20,pady=20)

while True:
    t = time.localtime(time.time())
    # localtime = time.asctime(t)
    # str = "Current Time:" + time.asctime(t)
    l['text']=time.asctime(t)
    w.update()
    # sleep(1)
    # t = time.localtime(time.time())
    # localtime = time.asctime(t)
    # str = "Current Time:" + time.asctime(t)
    # l=Label(w,text=str,font=("Goudy Stout",20))
    
w.mainloop()
