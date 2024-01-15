import pygame

pygame.init()

jetframe=[]

win=pygame.display.set_mode((1300,700))
frames=pygame.time.Clock()

# rocket1=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\rocket 1.png').convert_alpha()
# rocket1=pygame.transform.smoothscale(rocket1,(150,170))
# jetframe.append(rocket1)

rocket=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\rocket 1.png').convert_alpha()
rocket1=pygame.transform.smoothscale(rocket,(150,170))
rocket2=pygame.transform.scale(rocket,(150,170))

# rocket2=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\rocket 2.png').convert_alpha()
# rocket2=pygame.transform.scale(rocket2,(150,170))
# # jetframe.append(rocket2)

# rocket3=pygame.image.load('C:\\Users\\prithis\\Desktop\\py storage\\rocket store\\rocket 3.png').convert_alpha()
# rocket3=pygame.transform.scale(rocket3,(150,170))
# # jetframe.append(rocket3)


# jetframe.append(rocket1)
# jetframe.append(rocket2)
# jetframe.append(rocket1)
# jetframe.append(rocket2)
# jetframe.append(rocket3)


jetframe.append(rocket1)
# jetframe.append(rocket2)
# jetframe.append(rocket2)
# jetframe.append(rocket3)
# jetframe.append(rocket2)




f=0

while True:
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit(100)
            
    # f+=1
    # f%=len(jetframe)
    
    frames.tick(60)
    
    # pygame.draw.rect(win,'white',(100,100,300,300),30)
    # pygame.draw.line(win,'red',(100,100),(300,300),15)
    
    # win.blit(rocket1,(100,100))
    # win.blit(rocket2,(300,100))
    # win.blit(rocket3,(600,100))
    
    
    win.fill('black')

    # win.blit(jetframe[f],(100,100))

    win.blit(rocket1,(100,100))
    win.blit(rocket1,(400,100))
    
    
    # po=pygame.mouse.get_pos()
    # copo=jetframe[f].get_rect(center=po)
    # win.blit(jetframe[f],copo)    
    # print('good')
    pygame.display.update()
    pass

