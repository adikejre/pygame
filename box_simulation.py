import pygame
from sympy.solvers import solve
import random
from sympy.abc import a,b,c,v
import math
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
run=True
pygame.display.set_caption("my display")
blue=(0,0,150)
lblue=(239,13,231)
red=(255,255,153)
xb=100
yb=200
xs=500
ys=300
#v2=random.randint(1,4)
v2=0.0625
vel=v2
tenpow=random.randint(2,4)
m2=pow(10,tenpow)
m2=100
print(m2)
m1=10
#print(v2)
v1=0
count=0
def bigbox(x,y):
    pygame.draw.rect(screen,lblue,(x,y,200,200))


def smallbox(x,y):
    pygame.draw.rect(screen,blue,(x,y,100,100))


def collide(sx,bx):
    if(bx+200>=sx ):
        return True
    else:
        return False




while(run):
    #clock.tick(60)
    screen.fill((255,255,255))
    pygame.draw.rect(screen,red,(0,400,800,200))
    #pygame.display.update()
    # smallbox(xs,ys)
    # bigbox(xb,yb)
    if(xs>=700):
        v1=v1*(-1)
    # if(xs+v1<xb+v2):
    #     xs=xb
    if(collide(xs,xb)==True ):
        count+=1
        #eq=((m2/m1)*(v**2)-(2*m2*m2*vel*v/m1)-(m2*vel*vel*(1-m2/m1)))

        eq=(m2*v*v+(m1*v1*v1)+(m2*(v2-v)*(v2-v)*m2/m1)+(2*m2*v1*(v2-v))-m2*vel*vel)

        v2nlst=solve(eq,v)
        v11=(m2/m1)*(v2-v2nlst[0]) + v1
        v12=(m2/m1)*(v2-v2nlst[1]) + v1
        try:
            if(v11>0):
                v1=v11
                v2=v2nlst[0]
        except:
            if(v12>0):
                v1=v12
                v2=v2nlst[1]
    # if(collide(xs,xb)==True):
    #     if(v1<0)

    #if(v2!=0.0625):
        #print(v2)
    xb+=v2
    # if(xb+200==xs):
    #     print('yes')
    # if(xs<=xb+200):


    if(xs+v1<=700):
        xs+=v1
    else:
        xs=700-(v1-(700-xs))
        v1=v1*(-1)
    smallbox(xs,ys)
    bigbox(xb,yb)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()

print(count)
