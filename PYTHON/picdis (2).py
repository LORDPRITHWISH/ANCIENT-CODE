from tkinter import *
w=Tk()

pi = PhotoImage(file='C:\\Users\\prithis\\Desktop\\py storage\\cartr.png')

c=Canvas(w,width=600,height=600,bg="blue")
c.pack()
c.create_image(250,250,image=pi)

w.mainloop()