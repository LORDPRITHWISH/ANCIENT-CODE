import pygame

pygame.init()
W,H=1200,700
win=pygame.display.set_mode((W,H))

frame=pygame.time.Clock()
pygame.display.set_caption('lol')

font = pygame.font.Font('freesansbold.ttf',H)


count=0

while 1 :
    for event in pygame.event.get() :
    
        if event.type == pygame.QUIT :
            pygame.quit()
            exit(10)
        
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1 :  count+=1
            if event.button == 3 :  count=0

    # print(count)
    frame.tick(240)
    go=font.render(f'{count}',True,(220,220,255))
    gopo=go.get_rect(center=(W//2,H//2))
    if pygame.mouse.get_pressed()[0] :
        win.fill((0,0,150))
    elif pygame.mouse.get_pressed()[2] :
        win.fill((0,200,0))
    else :
        win.fill((0,0,0))
    win.blit(go,gopo)

    pygame.display.update()
