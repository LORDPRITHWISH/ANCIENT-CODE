from tkinter import *
import random
import time


bs=30
board=700
size=20
sns=board//size
fc="red"
sc="#29f21b"
shc="#056323"
scbg="#000a32"
sctg="#ffab00"
tg="#ffd000"
speed=100

class food:
    def __init__(self):
        x = random.randint(0, size-1) * sns
        y = random.randint(0, size-1) * sns

        self.cord = [x, y]
        # print("x: ",x,"  y: ",y)    
        # print(self.cord,"in food")

        c.create_oval(x, y, x + sns, y + sns, fill=fc, tags="food")

class snake:

    def __init__(self):
        self.body_size = bs
        self.cord = []
        self.sq = []


        for i in range(bs):
            self.cord.append([0,0])
        
        # print(sns)
        # print(self.cord)

        for x, y in self.cord:
            ns = c.create_rectangle(x, y, x + sns, y + sns, fill=sc, tags="snake")
            self.sq.append(ns)
            
        
def next_step():
    global score,f,s,p
    if st:
        x,y=s.cord[0]
        # print('reached 1')
        if d=="down":
            y+=sns
        elif d=="up":
            y-=sns
        elif d=="right":
            x+=sns
        elif d=="left":
            x-=sns
        # print("x: ",x,"  y: ",y) 
        
        if not bo:   
            x%=board
            y%=board
        ns = c.create_rectangle(x, y, x + sns, y + sns, fill=shc, tags="snake")
        s.sq.append(ns)
        s.cord.insert(0,[x,y])
        
        
        c.delete(s.sq[-2])
        del s.sq[-2]
        # print(s.sq[-2])
        ns = c.create_rectangle(s.cord[1][0], s.cord[1][1], s.cord[1][0] + sns,
                                s.cord[1][1] + sns, fill=sc, tags="snake")
        # print(s.cord[0][0], s.cord[0][1], s.cord[0][0] + sns, s.cord[0][1] + sns,('\t 1'))
        # print(s.cord[1][0], s.cord[1][1], s.cord[1][0] + sns, s.cord[1][1] + sns,('\t 2\n'))
        s.sq.insert(-1,ns)
        
        
        # c.coords(s.sq[0],s.cord[1][0], s.cord[1][1], s.cord[1][0] + sns+10, s.cord[1][1] + sns)
        # print("snake: ",s.cord[0],"  food:",f.cord,"in ns")
        if s.cord[0] == f.cord :
            # print(f.cord,"in cheak")
            c.delete("food")
            f=food()
            scorec.delete("score")
            score+=1
            scorec.create_text(scorec.winfo_width()//2,110,font=('Arial Black',50,'bold'),
                        text=f":{score:^5}:", fill=sctg, tags="score")
            # print("FOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\nFOOD\n")
        else:
            # print("del")
            c.delete(s.sq[0])
            del s.sq[0]
            s.cord.pop()
            # print(s.sq)
            # print(s.cord)
            # print('reached 2')
            
        if goc():
            go()
            
        else:             
            # print('reached 3') 
            if not p :
                p=True
                c.delete("start")
            w.after(speed,next_step)
    else:
        if p:
            c.create_text(c.winfo_width()//2, c.winfo_height()//2.2,
                        font=('Arial Black',300,'bold'), text="||", fill="white", tags="pause")
        else :
            c.create_text(c.winfo_width()//2, c.winfo_height()//2.2,
                        font=('Arial Black',30,'bold'), text="PRESS SPACE TO PLAY", fill="white", tags="start")

         
def goc():
    x,y=s.cord[0]
    if bo:
        if x<0 or x>=board or y<0 or y>=board:
            print("x: ",x,"  y: ",y) 
            
            return True
        
    if s.cord[0] in s.cord[1:]:        
        return True
    return False

# def goshow():
#     c.create_rectangle(s.cord[1][0], s.cord[1][1], s.cord[1][0] + sns, s.cord[1][1] + sns, fill=sc, tag="snake")

def go():
    c.create_rectangle(s.cord[0][0], s.cord[0][1], s.cord[0][0] + sns, s.cord[0][1] + sns, fill="red")
    c.create_text(c.winfo_width()/2, c.winfo_height()/3,font=('Kristen ITC',60,'bold'),
                  text="SORRY", fill="#ff2a00", tags="gameover")
    # print("why")
    w.update()
    time.sleep(2)
    # return
    c.delete(ALL)
    c.create_text(c.winfo_width()/2, c.winfo_height()/2,font=('Chiller',200,'bold'),
                  text="GAME\nOVER", fill="red", tags="gameover")

def dir(nd):
    global d
    if nd != d:
        if nd == "right" and d!="left":
            d=nd
        elif nd == "left" and d!="right":
            d=nd 
        elif nd == "up" and d!="down":
            d=nd 
        elif nd == "down" and d!="up":
            d=nd   
    # print("snake: ",s.cord[0],"  food:",f.cord,"in dir\n\n\n")

        
def stat():
    global st
    # print(st,"to")
    if st:
        st= not st
        # print('reached x')
        # print("snake: ",s.cord[0],"  food:",f.cord,"in stat sec t")

    else:
        st= not st
        c.delete("pause")
        # print("snake: ",s.cord[0],"  food:",f.cord,"in stat sec f")
        next_step()    
    # print(st)
    
def sp(a):
    # print('here')
    global speed
    if a=='+' and speed>10:
        speed-=10
    elif a=="-" :
        speed+=10
    else:
        print("uff")
    print(speed)
    
def re():
    global score,st,p,f,s,d
    score=0
    scorec.delete("score")
    scorec.create_text(scorec.winfo_width()//2,110,font=('Arial Black',50,'bold'),
                       text=f":{score:^5}:", fill=sctg, tags="score")
    c.delete(ALL)
    st=False
    p=False
    d="down"
    f=food()
    s=snake()
    next_step()

def bod():
    global bo
    if not p:
        bo=not bo
        if bo:
            b['text']=" ON "
        else:
            b['text']=" OFF "
        # print(bo)

w=Tk()
w.title("FOODIE SNAKE")

# st=True
p=False
st=False
bo=False
score=0

d="down"
c=Canvas(w,bg="black",height=board,width=board)
c.pack(side="left")
scorec=Canvas(w,bg=scbg,height=board,width=board//3)
scorec.pack(side="right")

bof=Frame(scorec,bg=scbg)

bf=Frame(scorec,bg=scbg)

bre=Button(bf,text=" RESTART ",font=("Cooper Black",12,'bold'),command=lambda: re())
bre.pack(side="left",padx=10)
be=Button(bf,text=" EXIT ",font=("Cooper Black",12,'bold'),command= w.destroy)
be.pack(side="left",padx=10)

w.bind("<Up>",lambda event: dir("up"))
w.bind("<Down>",lambda event: dir("down"))
w.bind("<Right>",lambda event: dir("right"))
w.bind("<Left>",lambda event: dir("left"))
w.bind("<space>",lambda event: stat())
w.bind("2",lambda event: dir("down"))
w.bind("4",lambda event: dir("left"))
w.bind("6",lambda event: dir("right"))
w.bind("8",lambda event: dir("up"))
w.bind("5",lambda event: stat())
w.bind("+",lambda event: sp('+'))
w.bind("-",lambda event: sp('-'))

bof.place(x=20,y=200)


l=Label(bof,font=("Cooper Black",14,'bold'),bg=scbg,fg=tg,text="BORDER :")
l.pack(side="left",padx=10)

b=Button(bof,font=("Cooper Black",10,'bold'),bg=scbg,fg=tg,text=" OFF ",command= lambda:bod())
b.pack(side="left")

w.update()
# print(sc.winfo_width())

bf.place(x=5,y=scorec.winfo_height()-50)



scorec.create_text(scorec.winfo_width()//2,50,font=('Arial Black',30,'bold','underline'),
                   text=f"SCORE", fill=sctg)
scorec.create_text(scorec.winfo_width()//2,110,font=('Arial Black',50,'bold'),
                   text=(f":{score:^5}:"), fill=sctg, tags="score")
sh = w.winfo_screenheight()-80
sw=w.winfo_screenwidth()
wh = w.winfo_height()
ww = w.winfo_width()
x=(sw-ww)//2
y=(sh-wh)//2
w.geometry(f"{ww}x{wh}+{x}+{y}")
w.resizable(False,False)
f=food()
s=snake()
next_step()
w.update()
w.mainloop()
