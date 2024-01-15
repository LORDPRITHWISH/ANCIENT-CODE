x=[410, 250,377, 224, 344, 172, 295, 144, 249, 145, 203, 180, 176, 215, 177, 260, 192, 304, 207, 338, 240, 367, 279, 401, 317, 432, 343, 463, 367, 486, 388, 511, 417, 548]
new=[]
k=[]
for i in range(0,len(x),2) :
    k.append(x[i])
xm=max(k)


for i in range(0,len(x),2) :
    # k.append(x[i])
    new.insert(0,x[i+1])
    new.insert(0,2*xm-x[i])

x.extend(new)

print(x)