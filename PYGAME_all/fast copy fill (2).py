import os
import shutil
import random
import string
import tqdm



path = 'H:\\test\\DARKNIGHT'

a=list(string.printable)
a=a[0:len(a)-2]
a.extend(list('\n '*5))
random.shuffle(a)
atext=''


tm=50      #text maker 100
fol=10     #no of folder 100
fil=50      #no of files 50
mul=10    #no of times text is writen 1000
num=0
def place() :
    global num
    while os.path.exists(f'{path}-{num}'):
        # shutil.rmtree(path)
        num+=1
    os.mkdir(f'{path}-{num}')

def text_maker() :
    global atext    
    for _ in range(tm**2):
        atext+=str(random.choice(a))    

def create() :
    os.mkdir(f'{path}-{num}\\LORD')

    for i in range(fil) :
        with open(f'{path}-{num}\\LORD\\PRITHWISH {i}.txt', 'w') as fi:
            # text_maker()
            fi.write(atext*mul)

def dupe() :
    for i in tqdm.tqdm(range(fol)) :
        shutil.copytree(f'{path}-{num}//LORD',f'{path}-{num}//LORD {i}')
        
def run() :
    place()
    text_maker()
    create()
    dupe()
    
run()