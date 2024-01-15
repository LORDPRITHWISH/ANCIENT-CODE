from tkinter import *
#import tkinter.font as font
def pri1():
    print("prithwish")
    b.config(text="HELLOW",background="red",foreground="yellow",command=lambda: pri2())
def pri2():
    print("prithwish")
    b.config(text="BOLO",background="GREEN",foreground="RED",command=lambda: pri1())
P=Tk()
#START
#myFont = font.Font(size=30)
P.title("DARKLORD")
P.geometry("900x600")
P.config(background="#3357e8")
b=Button(P,text="WOW",background="orange",width=30,height=10,foreground="yellow",command=lambda: pri1())
#b['font'] = myFont
b.pack()
#END
P.mainloop()

