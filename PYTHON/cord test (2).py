import math
def cord(d,l=10):
    k=True
    if d>70:
        d=140-d
        k=False
    d+=20
    s=math.tan(d*(math.pi/180))
    ss=s**2
    x=(l/(ss+1))**(1/2)
    y=x*s
    # print([x,y])
    if k :
        x=-x
    return [x,-y]

# for i in range(70):
#     print(cord(i))
print(cord(140-20))
print(cord(20))