from pygame import *
from tkinter import *

def play():
    mixer.music.play()
    print("playing")
    
def pause():
    mixer.music.pause()
    print('paused')

def resume():
    mixer.music.unpause()
    print('resume')
    
def quit():
    mixer.music.stop()
    print('stopped')

    
    

w=Tk()

w.title("sounds")
w.geometry('200x200+300+300')
mixer.init()
mixer.music.load('C:/Users/prithis/Desktop/CODE/work/bones.mp3')
bplay=Button(w,text='play',command= lambda: play())
bpause=Button(w,text='pause',command= lambda: pause())
bresume=Button(w,text='resume',command= lambda: resume())
bquit=Button(w,text='stop',command= lambda: quit())
bex=Button(w,text='exit',command= w.destroy)
bplay.pack()
bpause.pack()
bresume.pack()
bquit.pack()
bex.pack(pady=20)

w.mainloop()