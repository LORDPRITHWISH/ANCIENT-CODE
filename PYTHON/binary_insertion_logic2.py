a=[19, 53, 65, 74, 85, 4, 40, 91, 55, 3]





def sort(x) :
    for i in range(1,len(x)) :
        # print(x,x[i])
        
        p=getpos(x,i)
        v=x[i]
        x.pop(i)
        x.insert(p,v)
        
        
def getpos(x,c) :
    m,n,p=0,c-1,0
    while(m<=n):
        # print(F'M :{m} N :{n} P :{p}')
        
        p=(m+n)//2
        if x[p]==x[c] :
            return p

        elif x[p]>x[c]:
            n=p-1
        else:
            m=p+1
    if x[p]<x[c] :
        p+=1
    return p
    
print('IN : ',a)         
sort(a)
print('\n\nOUT: ',a)
