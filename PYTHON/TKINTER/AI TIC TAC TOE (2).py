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

# def stat2x():
#     global free
#     freespa()
    
#     r={1:[0,2],3:[0,6],5:[2,8],7:[6,8]}
#     for i in list(r.keys()):
#         if b[int(i/3)][i%3]['text']==p:
#             x=r[i]
#             break
#     print(x)
#     y=random.choice(x)
#     b[int(y/3)][y%3]['text']=a
#     return True
#     return False

def sin(x):
    if x==0:
        return 2
    if x==2:
        return 0
    if x==1:
        return 1
    
def stat1():
    if b[1][1]['text']=="":
        for i in [0,2,6,8] :
            if p == b[int(i/3)][i%3]['text'] :
                b[1][1]['text']=a
                return TRUE
    return False

def stat2():
    
    if len(free) == 8 and b[1][1]['text']=="":
        for i in [1,3,5,7] :
            r,c=int(i/3),i%3
            if p == b[r][c]['text'] :
                b[sin(r)][sin(c)]['text']=a
                return True
    return False

def stat3():
    print("in line")
    for i in [0,2,6,8]:
        if b[int(i/3)][i%3]['text']!="" :
            return False
    if b[1][1]['text']=="" and len(free) <= 8:
        print("got in")
        for i in [1,3,5,7] :
            if p == b[int(i/3)][i%3]['text'] :
                if i==1:
                    x=[6,8]
                elif i==3:
                    x=[2,8]
                elif i==5:
                    x=[0,6]
                elif i==7:
                    x=[0,2]
        y=random.choice(x)
        b[int(y/3)][y%3]['text']=a
        return True
    return False

def stat4():
    if b[1][1]['text']==p:
        global free
        freespa()
        rcl=[]
        for i in free:
            if i in [0,2,6,8]:
                rcl.append(i)
        print('ok')
        if (len(rcl) < 4) :
            print('good')
        rc=random.choice(rcl)
        b[int(rc/3)][rc%3]['text'] = a       
        return True 
    return False

def stat5():
    if b[1][1]['text']==a:
        global free
        freespa()
        if len(free)%2 == 0 :
            rcl=[]
            for i in free:
                if i in [1,3,5,7]:
                    rcl.append(i)
        
            rc=random.choice(rcl)
            b[int(rc/3)][rc%3]['text'] = a  
            
        else:
            for i in [1,3,5,7] :
                if p == b[int(i/3)][i%3]['text'] :
                    if i==1:
                        x=[6,8]
                    elif i==3:
                        x=[2,8]
                    elif i==5:
                        x=[0,6]
                    elif i==7:
                        x=[0,2]   
            
            y=random.choice(x)
            b[int(y/3)][y%3]['text']=a
        return True
    return False

def stat6():
    if empty():
        rcl=[0,1,2,3,4,5,6,7,8]        
        rc=random.choice(rcl)
        b[int(rc/3)][rc%3]['text'] = a
    return TRUE
      
def stat7():
    x=[0,2,6,8]
    for i in x:
        r,c=int(i/3),i%3
        if [r][c]['text'] == "":
            if [r+1][c]['text'] == a:
                if [r][c+1]['text'] == "":
                    if [r][c+2]['text'] == a:
                        [r][c]['text'] = a
                        return True
                if [r][c-1]['text'] == "":
                    if [r][c-2]['text'] == "":
                        [r][c]['text'] = a
                        return True
            if [r-1][c]['text'] == a:
                if [r][c+1]['text'] == "":
                    if [r][c+2]['text'] == a:
                        [r][c]['text'] = a
                        return True
                if [r][c-1]['text'] == "":
                    if [r][c-2]['text'] == "":
                        [r][c]['text'] = a
                        return True

        
def play():
    freespa()
    if stat1():
        pass
    elif stat2():
        pass
    elif stat3():
        pass
    elif stat4():
        pass
    elif stat5():
        pass
    elif stat6():
        pass
    elif stat7():
        pass
    else:
        sorry()

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

def empty():
    for i in range(3):
        for j in range(3):
            if b[i][j]['text']!="" :
                return False
    return True

def re():

    global p,a

    p = random.choice(Players)
    
    if(p == Players[1]):
        a=Players[0]
    else:
        a=Players[1]


    l["text"]=' YOUR TURN ( '+ p +' ) '

    for i in range(3):
        for j in range(3):
            b[i][j].config(text="",bg="white",fg="black")
    
    l.config(bg="white",fg="black")
    b3['state']=ACTIVE

def gofi():
    print('pressed')
    if empty():
        winch()
    b3['state']=DISABLED
    
    
#********************************************************************************************************   
w=Tk()
global p,a,free

w.resizable(False,False)

Players=['X','O']
p=random.choice(Players)
if(p == Players[1]):
    a=Players[0]
else:
    a=Players[1]

w.title("TIC TAC TOE")
l=Label(w,text=' YOUR TURN ( '+ p +' ) ',font=("Arial Black",20,'bold',),borderwidth=5,relief="raised")
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
b3=Button(f2,text="GO FIRST",font=("Arial Black",14),command=lambda:gofi())
b3.pack(side="right",padx=10)  
w.mainloop()