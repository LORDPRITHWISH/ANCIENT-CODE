from tqdm import*
a=sum(tqdm(range(100000000)))
def run(n) :
    total=0
    for i in range(5) :
        l=[j*1 for j in range(n)]
        # print(l)
        total+=sum(l)
    return total 

# print(run(10))
