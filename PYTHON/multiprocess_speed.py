import multiprocessing

def run(x,n):
    res=0
    for i in range(x):
        res+=i
    print(res,n)

r=100000000
mp=[]
if __name__ == "__main__":
    cpu=multiprocessing.cpu_count()
    print(cpu)
    for i in range(cpu):
        mp.append(multiprocessing.Process(target=run,args=(r,i),daemon=True))
        
    for i in mp :
        i.start()
    
    for i in mp :
        i.join()
    
    print('\n'*10,"done..")

    