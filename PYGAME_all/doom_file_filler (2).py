import os
import shutil
import random
import string
import tqdm
path = 'h:\\test\\DARKNIGHT'

a=list(string.printable)
a=a[0:len(a)-2]
a.extend(list('\n '*5))
random.shuffle(a)
atext=''


tm=50      #text maker
fol=100     #no of folder
fil=50      #no of files
mul=10    #no of times text is writen
num=0

def text_maker() :
    global atext    
    for _ in range(tm):
        atext+=str(random.choice(a))    

for _ in range(1000) :
        text_maker()
    
    
if os.path.exists(path):
    # os.rmdir(path)
    shutil.rmtree(path)
os.mkdir(path)


for i in tqdm.tqdm(range(fol)) :
    # print(i)
    infol=f'{path}//LORD {i}'
    os.mkdir(infol)
    
    for j in range(fil) :
        with open(f'{infol}\\PRITHWISH{j}.txt', 'w') as fi:
            # text_maker()
            fi.write(atext*mul)
