import math
def cord(d,l=1):
    s=round(math.tan(d*(math.pi/180)),3)
    # print(s)
    ss=s**2
    x=(l/(ss+1))**(1/2)
    return [x,x*s]

def distance(x):
    return ((x[0]**2)+(x[1]**2))**(1/2)
# print(cord(31.76,10))


# x=10

for x in range(5,100,5):
    print(x,' ',distance(cord(x,10)))
    # print(cord(x,10))