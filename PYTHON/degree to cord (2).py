import math
def cord(d,l=1):
    print('degree\t',d)
    r =d*(math.pi/180)
    print('redian\t',r)
    s=round(math.tan(r),3)
    print('slope\t',s)
    ss=s**2
    print('slope2\t',ss)
    print('l\t',l)
    ss1=ss+1
    print('(ss+1) ',ss1)
    x2=l/ss1
    
    print('x2\t',x2)
    x=x2**(1/2)
    print('x\t',x)
    y=x*s
    print('y\t',y)
    return [x,y]

# def yre(z,l):
#     return ((l**2)-(x**2))**(1/2)

def distance(z):
    return ((z[0]**2)+(z[1]**2))**(1/2)

def slope(z):
    return (z[0]/z[1])
# print(cord(45,1))
#  print(x,' ',distance(cord(x,10)))
x=105
k=cord(x,10)
print(x,' ',distance(k))
print('slope\t',slope(k))
print(k)