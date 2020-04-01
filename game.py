import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
run=True
pygame.display.set_caption("my display")
icon=pygame.image.load('animal-kingdom.png')
sp=pygame.image.load('myspace.jpg')
star=pygame.image.load('stars.png')
pygame.display.set_icon(icon)
x=400
y=500
def player(xx,yy):
    screen.blit(sp,(xx,yy))
def stars():
    xc=0
    yc=20
    while(xc<800):
        xc+=40
        yc=20
        while(yc<500):
            screen.blit(star,(xc,yc))
            yc+=30
        yc=40
        xc+=40
        while(yc<500):
            screen.blit(star,(xc,yc))
            yc+=30


while run:
    screen.fill((0,0,0))
    stars()
    player(x,y)

    #y-=0.2

    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x-=10
            if event.key==pygame.K_RIGHT:
                x+=10
            if event.key==pygame.K_UP:
                y-=10
            if event.key==pygame.K_DOWN:
                y+=10
        if x<=0:
            x=0
        elif y<=80:
            y=80
        elif y>=520:
            y=520
        elif x>=800:
            x=800
        player(x,y)


        pygame.display.update()
