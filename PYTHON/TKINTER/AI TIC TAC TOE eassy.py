from tkinter import *
import random 

def winai():
    
    for r in range(3):
        if b[r][0]['text']==b[r][1]['text'] == a and b[r][2]['text'] == "":
            b[r][2]['text']=a                           
            return True
        
        if b[r][2]['text']==b[r][1]['text'] == a and b[r][0]['text'] == "":
            b[r][0]['text']=a                           
            return True
        
        if b[r][0]['text']==b[r][2]['text'] == a and b[r][1]['text'] == "":
            b[r][1]['text']=a                           
            return True        
        
        
    for c in range(3):
        if b[0][c]['text']==b[1][c]['text'] == a and b[2][c]['text'] == "":
            b[2][c]['text']=a                           
            return True
        
        if b[2][c]['text']==b[1][c]['text'] == a and b[0][c]['text'] == "":
            b[0][c]['text']=a                           
            return True
        
        if b[0][c]['text']==b[2][c]['text'] == a and b[1][c]['text'] == "":
            b[1][c]['text']=a                           
            return True 
        
        
    if b[0][0]['text']==b[1][1]['text']==a and b[2][2]['text']=="":
        b[2][2]['text']=a
        return True
    if b[2][2]['text']==b[1][1]['text']==a and b[0][0]['text']=="":
        b[0][0]['text']=a
        return True
    if b[0][0]['text']==b[2][2]['text']==a and b[1][1]['text']=="":
        b[1][1]['text']=a
        return True
    
    
    if b[0][2]['text']==b[1][1]['text']==a and b[2][0]['text']=="":
        b[2][0]['text']=a
        return True
    if b[2][0]['text']==b[1][1]['text']==a and b[0][2]['text']=="":
        b[0][2]['text']=a
        return True   
    if b[0][2]['text']==b[2][0]['text']==a and b[1][1]['text']=="":
        b[1][1]['text']=a
        return True

def loseai():
    
    for r in range(3):
        if b[r][0]['text']==b[r][1]['text'] == p and b[r][2]['text'] == "":
            b[r][2]['text']=a                           
            return True
        
        if b[r][2]['text']==b[r][1]['text'] == p and b[r][0]['text'] == "":
            b[r][0]['text']=a                           
            return True
        
        if b[r][0]['text']==b[r][2]['text'] == p and b[r][1]['text'] == "":
            b[r][1]['text']=a                           
            return True        
        
    
    for c in range(3):
        if b[0][c]['text']==b[1][c]['text'] == p and b[2][c]['text'] == "":
            b[2][c]['text']=a                           
            return True
        
        if b[2][c]['text']==b[1][c]['text'] == p and b[0][c]['text'] == "":
            b[0][c]['text']=a                           
            return True
        
        if b[0][c]['text']==b[2][c]['text'] == p and b[1][c]['text'] == "":
            b[1][c]['text']=a                           
            return True 
        
        
    if b[0][0]['text']==b[1][1]['text']==p and b[2][2]['text']=="":
        b[2][2]['text']=a
        return True
    if b[2][2]['text']==b[1][1]['text']==p and b[0][0]['text']=="":
        b[0][0]['text']=a
        return True
    if b[0][0]['text']==b[2][2]['text']==p and b[1][1]['text']=="":
        b[1][1]['text']=a
        return True
    
    
    if b[0][2]['text']==b[1][1]['text']==p and b[2][0]['text']=="":
        b[2][0]['text']=a
        return True
    if b[2][0]['text']==b[1][1]['text']==p and b[0][2]['text']=="":
        b[0][2]['text']=a
        return True   
    if b[0][2]['text']==b[2][0]['text']==p and b[1][1]['text']=="":
        b[1][1]['text']=a
        return True
    
def aiev(): 
   
    for r in range(3):
        if b[r][0]['text']==b[r][1]['text'] == b[r][2]['text'] != "":
            if b[r][0]['text'] is a :              
                return 10
            if b[r][0]['text'] is p  :             
                return -10
                
    for c in range(3):
        if b[0][c]['text']==b[1][c]['text'] == b[2][c]['text'] != "":
            if b[0][c]['text'] is a   :            
                return 10
            if b[0][c]['text'] is p :           
                return -10
            
    if b[0][0]['text']==b[1][1]['text']==b[2][2]['text']!="":
        if b[0][0]['text'] is a :         
                return 10
        if b[0][0]['text'] is p  :             
            return -10
        
    if b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text']!="" :
        if b[2][0]['text'] is a  :            
                return 10
        if b[2][0]['text'] is p   :            
            return -10
    return 0
 
def freespa():
    global free
    free=[]
    for i in range (3):
            for j in range (3):                
                if b[i][j]['text'] == "": 
                    free.append((i*3+j))
    print(free)
    
 
def aitest(t):
    global free
    s=aiev()
    if s == -10 or 10:
        return s 
    
    if a:
        while(free):
            
            rc=random.choice(free)
            free.pop(free.index(rc))
            b[int(rc/3)][rc%3]['text'] = a
            m=aitest(not t)
            b[int(rc/3)][rc%3]['text'] = ""
        
        freespa()
    else:
        while(free):
            
            rc=random.choice(free)
            free.pop(free.index(rc))
            b[int(rc/3)][rc%3]['text'] = p
            m=aitest(not t)
            b[int(rc/3)][rc%3]['text'] = ""
        
        freespa()

def aipl():
    global free
    best=-10000
    
    while(free):
            
        rc=random.choice(free)
        free.pop(free.index(rc))
        b[int(rc/3)][rc%3]['text'] = a
        m=aitest(FALSE)
        b[int(rc/3)][rc%3]['text'] = ""
        
        if m > best:
            r,c=int(rc/3),rc%3
            best = m
    freespa()    
    b[r][c]['text'] = a
    
def stat1():
    global free
    freespa()
    rcl=[]
    for i in free:
        if i in [0,2,6,8]:
            rcl.append(i)
    
    rc=random.choice(free)
    b[int(rc/3)][rc%3]['text'] = a       
    return True 
    
def play():
    freespa()
    if stat1():
        pass
    elif stat2():
        pass
    elif aipl():        
        pass
    
def stat2():
    if b[1][1]['text']=="":
        if(bool(random.randint(0,2))):
            return FALSE
    b[1][1]['text']=a
    return TRUE
    
        



def ai():
    
    if winai():
        pass
    elif loseai():
        pass
    elif play():
        pass
    
    winner()  
       


def nt(r,c):
    global p
    if b[r][c]['text']=="" and winner() is False :
        b[r][c]['text']=p
        
        winch()
        
def winch():
    if(winner()=='tie'):
        print("fuck")   
    elif winner() :
        pass
    else:
        ai()

        
def winner():
    
    
   
    for r in range(3):
        if b[r][0]['text']==b[r][1]['text'] == b[r][2]['text'] != "":
            b[r][0].config(bg="green")
            b[r][1].config(bg="green")
            b[r][2].config(bg="green")
            l['text']=' '+b[r][0]['text']+' WINS '
            l.config(bg="green",fg="orange")                
            return True
                
    for c in range(3):
        if b[0][c]['text']==b[1][c]['text'] == b[2][c]['text'] != "":
            b[0][c].config(bg="green")
            b[1][c].config(bg="green")
            b[2][c].config(bg="green")
            l['text']=' '+b[0][c]['text']+' WINS '
            l.config(bg="green",fg="orange")
            return True
            
    if b[0][0]['text']==b[1][1]['text']==b[2][2]['text']!="":
        b[0][0].config(bg="green")
        b[1][1].config(bg="green")
        b[2][2].config(bg="green")
        l['text']=' '+b[0][0]['text']+' WINS '
        l.config(bg="green",fg="orange")
        return True
        
    if b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text']!="" :
        b[0][2].config(bg="green")
        b[1][1].config(bg="green")
        b[2][0].config(bg="green")
        l['text']=' '+b[0][2]['text']+' WINS '
        l.config(bg="green",fg="orange")
        return True
            
    
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
w.geometry="1600x1000"
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
        
        
w.mainloop()