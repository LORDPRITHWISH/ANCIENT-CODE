r=1000000000
for i in range(r+1):
    if i%(r//100)==0:
        print(i*100//r)
