import math
def insq(si):
    print(f"THE SIZE IS :  ",si)
    n=0
    for i in range(si) :    
        c=n
        for j in range(si) :
            # print(math.ceil(si/2)-n+c,"",c,end=" "*7)
            print(math.ceil(si/2)-n+c,end="  ")
            if j>(si-n-2) : c+=1
            elif c>0 : c-=1   
        # print(" "*10,n," "*10,i)
        print()
        if i== si/2-1 : pass
        elif i<si//2 : n+=1
        else : n-=1
insq(21)