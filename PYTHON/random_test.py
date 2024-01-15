import random as r
import string
import tqdm
size=10000000
a=list(string.ascii_uppercase)
li=[]
for _ in tqdm.tqdm(range(size)):
    str=""
    for _ in range(r.randint(0,11)):
        str+=r.choice(a)
    li.append(str)    
avg=0    
for i in tqdm.tqdm(li) :
    avg+=len(i)
avg/=size    

print(avg)
# print(li)

# r.choice