from tkinter import *
import random 

def aitest(x):
    
    for r in range(3):
        if b[r][0]['text']==b[r][1]['text'] == x and b[r][2]['text'] == "":
            b[r][2]['text']=a                       
            return True
        
        if b[r][2]['text']==b[r][1]['text'] == x and b[r][0]['text'] == "":
            b[r][0]['text']=a                           
            return True
        
        if b[r][0]['text']==b[r][2]['text'] == x and b[r][1]['text'] == "":
            b[r][1]['text']=a                           
            return True        
        
        
    for c in range(3):
        if b[0][c]['text']==b[1][c]['text'] == x and b[2][c]['text'] == "":
            b[2][c]['text']=a                          
            return True
        
        if b[2][c]['text']==b[1][c]['text'] == x and b[0][c]['text'] == "":
            b[0][c]['text']=a                          
            return True
        
        if b[0][c]['text']==b[2][c]['text'] == x and b[1][c]['text'] == "":
            b[1][c]['text']=a                        
            return True 
        
        
    if b[0][0]['text']==b[1][1]['text']==x and b[2][2]['text']=="":
        b[2][2]['text']=a
        return True
    if b[2][2]['text']==b[1][1]['text']==x and b[0][0]['text']=="":
        b[0][0]['text']=a
        return True
    if b[0][0]['text']==b[2][2]['text']==x and b[1][1]['text']=="":
        b[1][1]['text']=a
        return True
    
    
    if b[0][2]['text']==b[1][1]['text']==x and b[2][0]['text']=="":
        b[2][0]['text']=a
        return True
    if b[2][0]['text']==b[1][1]['text']==x and b[0][2]['text']=="":
        b[0][2]['text']=a
        return True   
    if b[0][2]['text']==b[2][0]['text']==x and b[1][1]['text']=="":
        b[1][1]['text']=a
        return True

    
def freespa():
    global free
    free=[]
    for i in range (3):
            for j in range (3):                
                if b[i][j]['text'] == "": 
                    free.append((i*3+j))
    print(free)
    
def stat2():
    if b[1][1]['text']==p:
        global free
        freespa()
        rcl=[]
        for i in free:
            if i in [0,2,6,8]:
                rcl.append(i)
        
        rc=random.choice(rcl)
        b[int(rc/3)][rc%3]['text'] = a       
        return True 
    return False

def stat3():
    if b[1][1]['text']==a:
        global free
        freespa()
        rcl=[]
        for i in free:
            if i in [1,3,5,7]:
                rcl.append(i)
        
        rc=random.choice(rcl)
        b[int(rc/3)][rc%3]['text'] = a       
        return True 
    return False

def stat4():
    global free
    freespa()        
    rc=random.choice(free)
    b[int(rc/3)][rc%3]['text'] = a
    
def play():
    freespa()
    if stat1():
        pass
    elif stat2():
        pass
    elif stat3():
        pass
    else:
        stat4()
    
def stat1():
    if b[1][1]['text']=="":
        for i in [0,1,2,3,5,6,7,8] :
            if p == b[int(i/3)][i%3]['text'] :
                b[1][1]['text']=a
                return TRUE
    return False
    
        



def ai():
    
    if aitest(a):
        pass
    elif aitest(p):
        pass
    elif play():
        pass
    
    wite()  
       


def nt(r,c):
    global p
    if b[r][c]['text']=="" and winner() is False :
        b[r][c]['text']=p
        
        winch()

def winch():
    if wite():
        ai()
        
def wite():
    if(winner()=='tie'):
        pass 
    elif winner() is a :
        l['text']=' AI WINS '
        l.config(bg="yellow",fg="red")
    elif winner() is p:
        l['text']=' YOU WIN '
        l.config(bg="green",fg="orange")
    else:
        return True
    return False

        
def winner():
    
    
   
    for r in range(3):
        if b[r][0]['text']==b[r][1]['text'] == b[r][2]['text'] != "":
            b[r][0].config(bg="green")
            b[r][1].config(bg="green")
            b[r][2].config(bg="green")
            return b[r][0]['text']
                
    for c in range(3):
        if b[0][c]['text']==b[1][c]['text'] == b[2][c]['text'] != "":
            b[0][c].config(bg="green")
            b[1][c].config(bg="green")
            b[2][c].config(bg="green")
            return b[0][c]['text']
            
    if b[0][0]['text']==b[1][1]['text']==b[2][2]['text']!="":
        b[0][0].config(bg="green")
        b[1][1].config(bg="green")
        b[2][2].config(bg="green")
        return b[0][0]['text']
        
    if b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text']!="" :
        b[0][2].config(bg="green")
        b[1][1].config(bg="green")
        b[2][0].config(bg="green")
        return b[0][2]['text']
            
    
    if progress():
        print("TIE")
        for i in range(3):
            for j in range(3):
                b[i][j].config(bg="red",fg="yellow")
                
        l['text']=" SORRY! IT'S A TIE "
        l.config(bg="yellow",fg="red")
        return 'tie'
        
    return False
    

def progress():
    for i in range(3):
        for j in range(3):
            if b[i][j]['text']=="" :
                return False
    return True


def re():

    global p,a

    p = random.choice(Players)
    
    if(p == Players[1]):
        a=Players[0]
    else:
        a=Players[1]


    l["text"]=' STARTING '+p+'\'s TURN '

    for i in range(3):
        for j in range(3):
            b[i][j].config(text="",bg="white",fg="black")
    
    l.config(bg="white",fg="black")
    
   
#********************************************************************************************************   
w=Tk()

global p,a,free

Players=['X','O']
p=random.choice(Players)
if(p == Players[1]):
    a=Players[0]
else:
    a=Players[1]

w.title("TIC TAC TOE")
l=Label(w,text=' STARTING '+p+'\'s TURN ',font=("Arial Black",20,'bold',),borderwidth=5,relief="raised")
l.pack(side="top")
f=Frame(w,background="blue",border=5)
f.pack(side="top",pady=15,padx=15,fill=X)
b=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        # b[i][j]=Button(f,font=("Arial Black",40),width=4)
        # b[i][j].grid(row=i,column=j)
        b[i][j] = Button(f, text="",font=('Arial Black',50,'bold'), width=3, height=1,command= lambda r=i, c=j: nt(r,c))
        b[i][j].grid(row=i,column=j)

f2=Frame(w)
f2.pack(side="bottom",padx=10,pady=5)
b1=Button(f2,text="RESTART",font=("Arial Black",14),command=lambda:re())
b1.pack(side='right',padx=10)

b2=Button(f2,text="EXIT",font=("Arial Black",14),width=4,command= w.destroy)
b2.pack(side='left',padx=10)
        
sh = w.winfo_screenheight()
sw=w.winfo_screenwidth()
h = w.winfo_height()
wi = w.winfo_width()
g=w.winfo_geometry()

w.update()

print(h)
print(wi)
print(sh)
print(sw)
print(g)
        
w.mainloop()
