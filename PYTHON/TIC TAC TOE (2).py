from tkinter import *
import random 



def nt(r,c):
    global p
    
    if b[r][c]['text']=="" and winner() is False :
        b[r][c]['text']=p
        
        if(winner()=='tie'):
            print("fuck")   
        elif winner() :
            l['text']=' '+p+' WINS '
            l.config(bg="green",fg="orange")

        else:
            print('shit')
            
            if(p==Players[0]):
                p=Players[1]
                l['text']=' '+p+'\'s TURN '
                
            elif(p==Players[1]):
                p=Players[0]
                l['text']=' '+p+'\'s TURN '
            


        
def winner():
    global p
    
   
    for r in range(3):
        if b[r][0]['text']==b[r][1]['text'] == b[r][2]['text'] != "":
            b[r][0].config(bg="green")
            b[r][1].config(bg="green")
            b[r][2].config(bg="green")                
            return True
                
    for c in range(3):
        if b[0][c]['text']==b[1][c]['text'] == b[2][c]['text'] != "":
            b[0][c].config(bg="green")
            b[1][c].config(bg="green")
            b[2][c].config(bg="green")
            l['text']=' '+p+' WINS '
            l.config(bg="green",fg="orange")
            return True
            
    if b[0][0]['text']==b[1][1]['text']==b[2][2]['text']!="":
        b[0][0].config(bg="green")
        b[1][1].config(bg="green")
        b[2][2].config(bg="green")
        l['text']=' '+p+' WINS '
        return True
        
    if b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text']!="" :
        b[0][2].config(bg="green")
        b[1][1].config(bg="green")
        b[2][0].config(bg="green")
        l['text']=' '+p+' WINS '
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

    global player

    player = random.choice(Players)

    l["text"]=' STARTING '+p+'\'s TURN '

    for i in range(3):
        for j in range(3):
            b[i][j].config(text="",bg="white",fg="black")
    
    l.config(bg="white",fg="black")
    
    
    
    
    
    
    
    
    
w=Tk()

global p
Players=['X','O']
p=random.choice(Players)


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