import pygame


pygame.init()
win=pygame.display.set_mode((1300,700))
frame=pygame.time.Clock()
a=b=c=0
ai,bi,ci=1,2,3
# ad=bd=cd=False
r=15
while True :
    for eve in pygame.event.get() :
            if eve.type == pygame.QUIT :
                pygame.quit()
                exit(10)
    win.fill((a,b,c))
    a+=ai;b+=bi;c+=ci
    if a>240 :
        ai+=1
        ai%=r
        ai=-ai
    elif a<25 :
        ai=-ai
        ai+=2
        ai%=r
        
    if b>240 :
        bi+=3
        bi%=r
        bi=-bi
    elif b<25 :
        bi=-bi
        bi+=1
        bi%=r
        
    if c>240 :
        ci+=1
        ci%=r
        ci=-ci
    elif c<25 :
        ci=-ci
        ci+=4
        ci%=r
    print(a,b,c)
    
    
    pygame.display.update()
    frame.tick(60)