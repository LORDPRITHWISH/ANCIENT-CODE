from tkinter import *
# global i
# i=0
# # def next():
# #     d=c.create_rectangle(i+=100,i+=100,(i+=100)+100,(i+=100)+100,fill="green")
# def next(dir):
#     global i,des
#     if dir == "left":
#         i-=100
#     elif dir == "right":
#         i+=100
#     d=c.create_rectangle((i),(i),(i+100),(i+100),fill="green")
#     des.append(d)
#     print(des,"\t add")

    

# def de():
#     global des
#     print("ho")
#     c.delete(des[0])
#     des.pop(0)
#     print(des),'\t del'
    
w=Tk()
# des=[]
c=Canvas(w,height=600,width=600,bg="brown",)
c.pack()

d=c.create_rectangle(0,0,100,100,fill="green")
des.append(d)

d=c.create_rectangle(50,50,300,400,fill="blue")


w.bind("<Left>",lambda event: next("left"))
w.bind("<Right>",lambda event: next("right"))
w.bind("1",lambda event: de())


r=c.create_rectangle(50,50,300,400,fill="blue")
d=r
c.delete(d)
# del d

w.mainloop()