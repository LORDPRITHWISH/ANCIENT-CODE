class dumb :
    def __init__(self) -> None:
        self.a=20
        self.b=40
    
    def ass(self):
        self.c=self.a+self.b
        print(self.c)
        
    def sub(self):
        self.d=self.c-self.b
        print(self.d)
        
    def  eqal(self):
        if self.a==self.d :
            print ('good')
            
    def outy(self,p,q) :
        return(p**q)

# d=dumb()
# d.ass()
# d.sub()
# d.eqal()
