import pygame
import time
import random
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('visualization')
run=True
blue=(0,0,150)
lblue=(229,204,255)
h=[]
n=random.randint(5,30)
print(n)
i=0
while(i<n):
    h.append(random.randint(20,400))
    i+=1
#print(h)

#draw.rect(a,b,c,d) where a,b=x,y coordinate of top left
#c=width,d=height
while run:
    screen.fill((255,255,255))
    i=0
    while(i<n):
        pygame.draw.rect(screen,blue,(40+24*i,595-h[i],20,h[i]))
        i+=1
    i=0
    while(i<n):
        pygame.draw.rect(screen,lblue,(40+24*i,595-h[i],20,h[i]))
        i+=1

        pygame.display.update()
        clock.tick(25)
        #time.sleep(100)



    mouse=pygame.mouse.get_pos()
    #print(mouse)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
