import pygame as pg  

# define constants  
WIDTH = 500  
HEIGHT = 500  
FPS = 60  

# define colors  
BLACK = (0 , 0 , 0)  
GREEN = (0 , 255 , 0)  


ver,hor=0,0

AMM=5
# initialize pggame and create screen  
pg.init()  
screen = pg.display.set_mode((WIDTH , HEIGHT))  
# for setting FPS  
clock = pg.time.Clock()  

rot = 0  
rot_speed = 2  

# define a surface (RECTANGLE)  
image_orig = pg.Surface((100 , 100))  
# for making transparent background while rotating an image  
image_orig.set_colorkey(BLACK)  
# fill the rectangle / surface with green color  
image_orig.fill(GREEN)  
# creating a copg of orignal image for smooth rotation  
image = image_orig.copy()  
image.set_colorkey(BLACK)  
# define rect for placing the rectangle at the desired position  
rect = image.get_rect()  
rect.center = (WIDTH // 2 , HEIGHT // 2)  
# keep rotating the rectangle until running is set to False  
running = True  
while running:  
    # set FPS  
    clock.tick(FPS)  
    # clear the screen every time before drawing new objects  
    screen.fill(BLACK)  
    # check for the exit  
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            running = False  
        if event.type == pg.KEYDOWN :
                # obsticle(random.randint(20,WI))
                if event.key == pg.K_w or event.key == pg.K_UP :
                    ver-=AMM
                if event.key == pg.K_a or event.key == pg.K_LEFT :
                    hor-=AMM
                if event.key == pg.K_s or event.key == pg.K_DOWN :
                    ver+=AMM
                if event.key == pg.K_d or event.key == pg.K_RIGHT :
                    hor+=AMM


        if event.type == pg.KEYUP :
                # obsticle(random.randint(20,WI))
                if event.key == pg.K_w or event.key == pg.K_UP :
                    ver+=AMM
                if event.key == pg.K_a or event.key == pg.K_LEFT :
                    hor+=AMM
                if event.key == pg.K_s or event.key == pg.K_DOWN :
                    ver-=AMM
                if event.key == pg.K_d or event.key == pg.K_RIGHT :
                    hor-=AMM

    # making a copg of the old center of the rectangle  
    old_center = rect.center  
    print(old_center)
    # old_center[1]+=10
    # old_center[1]%=HEIGHT
    old_center=((old_center[0]+hor)% WIDTH,(old_center[1]+ver)% HEIGHT)
    print(old_center)
    # defining angle of the rotation  
    # rot = (rot + rot_speed) % 360  
    # if hor :
    rot=9*hor
    # rotating the orignal image  
    new_image = pg.transform.rotate(image_orig , rot)  
    rect = new_image.get_rect()  
    # set the rotated rectangle to the old center  
    rect.center = old_center  
    # drawing the rotated rectangle to the screen  
    screen.blit(new_image , rect)  
    # flipping the display after drawing everything  
    pg.display.flip()  

pg.quit()  