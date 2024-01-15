# from pygame import *
import pygame
# import threading
import time
import random
pygame.init()

WI,HI=1300,700
# WI,HI=1000,500

win=pygame.display.set_mode((WI,HI))
# win=pygame.display.set_mode((1000,500))

frames=pygame.time.Clock()

jetframe=[]

# ship=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket_trans.png').convert_alpha()
# ship=pygame.transform.scale(ship,(110,120))

rocket1=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\rocket 1.png').convert_alpha()
rocket1=pygame.transform.smoothscale(rocket1,(150,170))
# frame.append(rocket1)

rocket2=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\rocket 2.png').convert_alpha()
rocket2=pygame.transform.smoothscale(rocket2,(150,170))
# frame.append(rocket2)

rocket3=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\rocket 3.png').convert_alpha()
rocket3=pygame.transform.smoothscale(rocket3,(150,170))
# frame.append(rocket3)

back=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\space.png').convert_alpha()
back=pygame.transform.smoothscale(back,(1300,700))

commet=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\commet.png').convert_alpha()
# commet=pygame.transform.scale(commet,(150,150))
commet=pygame.transform.smoothscale(commet,(50,100))


labu=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\bullet.png').convert_alpha()
labu=pygame.transform.smoothscale(labu,(20,50))

rabu=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\laser beam.png').convert_alpha()
rabu=pygame.transform.smoothscale(rabu,(20,80))


jetframe.append(rocket1)
jetframe.append(rocket2)
jetframe.append(rocket2)
jetframe.append(rocket3)
jetframe.append(rocket2)


comcou=[]
lapo=[]
redla=[]

font = pygame.font.Font('freesansbold.ttf',150)
go=font.render(":  GAME OVER  :",True,(255,0,0))

def over() :
    # print('over')
    po=go.get_rect(center=(1300//2,700//2))
    time.sleep(.2)
    win.fill('black')
    win.blit(go,po)
    pygame.display.update()
    # print('OVER')
    time.sleep(1)
    exit(10000)

def obsticle(e) :
    # print(e)
    e=(e,0)
    compo=commet.get_rect(midbottom=e)
    
    comcou.append([compo,2])
    # print(e)
    # print(compo)
    
    
def bullet() :
    buco=labu.get_rect(center=pygame.mouse.get_pos())
    d=30
    buco[0]+=d    
    lapo.append(buco[::])
    buco[0]-=(2.1*d)
    lapo.append(buco)
    # bulrate.tick(3)

def laser(e) :
    buco=rabu.get_rect(center=e)
    redla.append(buco)
        
e=False
comti=100
buti=0
jetfr=0

while True:
    
    jetfr+=1
    jetfr%=len(jetframe)
    for event in pygame.event.get() :
    
        if event.type == pygame.QUIT :
            pygame.quit()
            exit(100)
        
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1 :  e=True
            
            if event.button == 3 :
                laser(event.pos)
                obsticle(event.pos[0])
                # print('good',event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP :
            if event.button == 1 :
                e=False
                buti=0
                bullet()
        if event.type == pygame.KEYDOWN :
            # obsticle(random.randint(20,WI))
            if event.key == pygame.K_SPACE :
                # print('pressed')
                obsticle(pygame.mouse.get_pos()[0])
            if event.key == pygame.K_a :
                print('pressed')
                bullet()
    
    frames.tick(50)
    win.blit(back,(0,0))
    
    
    for i in comcou :
        i[0][1]+=2
        # print(i)
        # pygame.draw.rect(win,'white',i[0],3)
        
        win.blit(commet,i[0])
        if i[0][1] >650 :
            # print(i)
            comcou.remove(i)
        
    
    for i in lapo :
        i[1]-=10
        # pygame.draw.rect(win,'white',i,3)
        
        win.blit(labu,i)
        if i[1]<0 :
            # print(i)
            lapo.remove(i)
    
    for i in redla :
        i[1]-=7
        # pygame.draw.rect(win,'white',i,3)
        
        win.blit(rabu,i)
        if i[1]<0 :
            # print(i)
            redla.remove(i)
            
    for i,p in enumerate(comcou) :
        
        for j in redla :
            # i=tuple()
            if p[0].colliderect(j) :
                comcou.pop(i)
                break
        else :
            for j in lapo :
                # i=tuple()
                if p[0].colliderect(j) :
                    lapo.remove(j)
                    if p[1]<0 : 
                        comcou.remove(p)
                        break
                    else :
                        print(p[1])
                        comcou[i][1]-=1    
                    break
    
    po=pygame.mouse.get_pos()
    copo=jetframe[jetfr].get_rect(center=po)
    win.blit(jetframe[jetfr],copo)
    # pygame.draw.rect(win,'white',copo,3)
    
    
    if e :
        if buti==0:
            buti=5
            buco=labu.get_rect(center=po)
            d=30
            buco[0]+=d
            lapo.append(buco[::])
            buco[0]-=(2.1*d)
            lapo.append(buco)
            # bulrate.tick(3)
            
        buti-=1
    
    for i in comcou :
        if i[0].colliderect(copo) :
            over()
            
    if comti==0 :
        comti=random.randint(10,50)
        obsticle(random.randint(20,WI))
        print('IT IS ',comti)
    comti-=1
    # print(comti)
    
    
    pygame.display.update()

