import random
# aa=[[x,x*100+x] for x in range(1,10)]
a=[x for x in range(1,10)]
b=[x*100+x for x in range(1,10)]
random.shuffle(a)
random.shuffle(b)

c=list(zip(a,b))
random.shuffle(c)
print(c)

c.sort(key=lambda a :a[1])
print(c)

