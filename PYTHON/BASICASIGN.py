from tkinter import *
menu={'FISH FRY':80,'BIRIYANI':120,'CHILI CHICKEN':230,'PIZZA':315,'MUTTON CHAP':440}
def assign():
    for i in menu :
        x.insert(x.size(),i+' : $'+str(menu.get(i)))
    if x.size()>7 :
        x.config(height=x.size()) 
        y.config(height=x.size())

def add():
    for i in x.curselection() :
        ch=True
        new=x.get(i)
        for j in range(y.size()):
            old=y.get(j)        
            if new==old.split('*')[0] :
                y.delete(j)
                y.insert(i,x.get(i)+'*'+str(int(old.split('*')[1])+1))
                ch=False
                break
        if ch :
            y.insert(y.size(),x.get(i)+'*1')
        
def remove():
    for i in reversed(y.curselection()) :
        y.delete(i)
        
def bill() :
    bwin=Toplevel()
    bwin.title('BILL')
    z=Listbox(bwin,font=('Cooper Black',20),width=25)
    z.pack(side='left')
    tot=0
    for i in range(y.size()):
        k=y.get(i)
        z.insert(i,k)
        p=k.split('$')[1]
        tot+=int(p.split('*')[0])*int(p.split('*')[1])
    tot=str(tot)    
    z.insert(z.size(),'-'*70)
    z.insert(z.size(),'TOTAL IS : '+tot)
    if z.size()>7 :
        z.config(height=x.size())
    bwin.mainloop()
    
w=Tk()
w.title('FOOD ODERING MENU PROGRAM')
x=Listbox(w,font=('Cooper Black',20),width=25,selectmode=MULTIPLE)
x.pack(side='left')
y=Listbox(w,font=('Cooper Black',20),width=30,selectmode=MULTIPLE)
y.pack(side='right')
add_button=Button(w,text='ADD',command=lambda:add())
add_button.pack(pady=10)
remove_button=Button(w,text='REMOVR',command=lambda:remove())
remove_button.pack(pady=10)
billbutton=Button(w,text='BILL',command=lambda:bill())
billbutton.pack(pady=10)
ex=Button(w,text='EXIT',command=w.destroy)
ex.pack(pady=10)
assign()
w.mainloop()