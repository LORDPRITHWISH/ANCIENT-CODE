a=[19, 53, 65, 74, 85, 4, 40, 91, 55, 3]
# a=[3,9,5,4,2,10]


def short(x):
    # print(id(x))
    for i in range(1,len(x)) :
        # print(x,x[i])
        # for j in range(i)
        m,n=0,i-1
        while(m<=n):
            p=(m+n)//2
            # print(F'M :{m} N :{n} P :{p}')
            
            if x[p]==x[i] :
                v=x[i]
                x.pop(i)
                x.insert(p,v)
                # print(F'END M :{m} N :{n} P :{p}')
                break
            
            elif x[p]>x[i] :
                if x[p-1]<x[i] or p==0:
                    v=x[i]
                    x.pop(i)
                    x.insert(p,v)
                    # print(F'END M :{m} N :{n} P :{p}')
                    break
                n=p-1
            else :
                if x[p+1]>x[i]:
                    v=x[i]
                    x.pop(i)
                    x.insert(p+1,v)
                    # print(F'END M :{m} N :{n} P :{p}')
                    break
                m=p+1
            # print(F'END M :{m} N :{n} P :{p}')
            # if abs(m-n) == 1 :
            #     print('broke')
            #     break
        
        # v=x[i]
        # x.pop(i)
        # x.insert(p,v)
                
    # print(id(x))
    return(x)
       
print('IN : ',a)         
short(a)
print('OUT: ',a)
                
# print(a)
# print(short(a))

