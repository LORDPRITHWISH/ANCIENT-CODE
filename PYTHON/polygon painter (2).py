from tkinter import *
co=[]
def draw( e ) :
    global co
    co.append(e.x)
    co.append(e.y)
    print(co)
    c.delete('base')
    c.create_polygon(co,fill='white',tags='base')

def mandraw():
    pos=[377, 224, 344, 172, 295, 144, 249, 145, 203, 180, 176, 215, 177, 260, 192, 304, 207, 338, 240, 367, 279, 401, 317, 432, 343, 463, 367, 486, 388, 511, 417, 548]
    pos=[425, 250, 377, 224, 344, 172, 295, 144, 249, 145, 203, 180, 176, 215, 177, 260, 192, 304, 207, 338, 240, 367, 279, 401, 317, 432, 343, 463, 367, 486, 388, 511, 417, 548, 433, 548, 462, 511, 483, 486, 507, 463, 533, 432, 571, 401, 610, 367, 643, 338, 658, 304, 673, 260, 674, 215, 647, 180, 601, 145, 555, 144, 506, 172, 473, 224, 425, 250]

    c.create_polygon(pos,fill='white',tags='base')
w=Tk()

c=Canvas(w,height=650,width=800,bg='black')
c.pack()
w.bind("<Button-1>",draw)

mandraw()

w.mainloop()