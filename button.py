import pygame
#import time
import random
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption('visualization')
run=True
blue=(0,0,150)
lblue=(229,204,255)
white=(255,255,255)
red=(255,255,153)
green=(153,255,204)
black=(0,0,0)
h=[]
n=random.randint(68,80)
print(n)
i=0
while(i<n):
    h.append(random.randint(20,400))
    i+=1
#print(h)
i=0
k=0
m=0
p=0
q=0
def merge(arr,l,m,r):

    n1 = m - l + 1
    n2 = r- m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2 :
        clock.tick(15)
        if L[i] <= R[j]:
            pygame.draw.rect(screen,white,(20+12*(l+i),150,10,595))
            pygame.draw.rect(screen,white,(20+12*(m+j+1),250,10,595))
            pygame.draw.rect(screen,lblue,(20+12*(l+i),595-arr[l+i],10,arr[l+i]))
            pygame.draw.rect(screen,lblue,(20+12*(m+j+1),595-arr[m+j+1],10,arr[m+j+1]))
            pygame.display.update()
            pygame.time.wait(100)
            #clock.tick(20)
            pygame.draw.rect(screen,blue,(20+12*(l+i),595-arr[l+i],10,arr[l+i]))
            pygame.draw.rect(screen,blue,(20+12*(m+j+1),595-arr[m+j+1],10,arr[m+j+1]))
            pygame.display.update()
            arr[k] = L[i]
            pygame.draw.rect(screen,white,(20+12*(k),150,10,595))
            pygame.draw.rect(screen,blue,(20+12*(k),595-arr[k],10,arr[k]))

            i += 1

            pygame.display.update()
            #clock.tick(20)

        else:
            #rekt=(40+24*(m+j+1),0,20,595)
            pygame.draw.rect(screen,white,(20+12*(k),150,10,595))
            pygame.draw.rect(screen,white,(20+12*(m+j+1),150,10,595))
            pygame.draw.rect(screen,lblue,(20+12*(k),595-arr[k],10,arr[k]))
            pygame.draw.rect(screen,lblue,(20+12*(m+j+1),595-arr[k],10,arr[k]))
            pygame.display.update()
            pygame.time.wait(100)
            #clock.tick(20)
            pygame.draw.rect(screen,blue,(20+12*(m+j+1),595-arr[k],10,arr[k]))
            pygame.draw.rect(screen,blue,(20+12*(m+j+1),595-arr[k],10,arr[k]))
            pygame.display.update()
            arr[k] = R[j]
            pygame.draw.rect(screen,white,(20+12*(k),150,10,595))
            pygame.draw.rect(screen,blue,(20+12*(k),595-arr[k],10,arr[k]))
            j += 1



            pygame.display.update()
            #clock.tick(20)
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        clock.tick(15)
        pygame.draw.rect(screen,white,(20+12*(l+i),150,10,595))
        pygame.draw.rect(screen,lblue,(20+12*(l+i),595-arr[l+i],10,arr[l+i]))

        pygame.display.update()
        pygame.time.wait(100)
        #clock.tick(20)
        pygame.draw.rect(screen,blue,(20+12*(l+i),595-arr[l+i],10,arr[l+i]))
        pygame.display.update()
        arr[k] = L[i]
        pygame.draw.rect(screen,white,(20+12*(k),150,10,595))
        pygame.draw.rect(screen,blue,(20+12*(k),595-arr[k],10,arr[k]))
        i += 1
        pygame.display.update()
        #clock.tick(20)
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        clock.tick(15)
        pygame.draw.rect(screen,white,(20+12*(m+j+1),150,10,595))
        pygame.draw.rect(screen,lblue,(20+12*(j+m+1),595-arr[j+m+1],10,arr[j+m+1]))

        pygame.display.update()
        pygame.time.wait(100)
        #clock.tick(20)
        pygame.draw.rect(screen,blue,(20+12*(m+j+1),595-arr[j+m+1],10,arr[j+m+1]))
        pygame.display.update()
        arr[k] = R[j]
        pygame.draw.rect(screen,white,(20+12*(k),150,10,595))
        pygame.draw.rect(screen,blue,(20+12*(k),595-arr[k],10,arr[k]))
        j += 1

        pygame.display.update()
        #clock.tick(20)
        k+=1

#merge ends
def mergesort(ar,l,r):


    if l<r:
        m=(l+r)//2
        mergesort(ar,l,m)
        mergesort(ar,m+1,r)
        merge(ar,l,m,r)


z=0
x=0
mm=0
start=-1
mer=[]
ins=[]
while(mm<n) :
    mer.append(h[mm])
    ins.append(h[mm])
    mm+=1

#draw.rect(a,b,c,d) where a,b=x,y coordinate of top left
#c=width,d=height
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface, textsurface.get_rect()



font = pygame.font.Font('freesansbold.ttf', 15)
textsurf1,textRect1= text_objects("Start",font)
textsurf2,textRect2= text_objects("Merge Sort",font)
textsurf3,textRect3= text_objects("Insertion Sort",font)

textRect1.center= (80,60)
textRect2.center= (200,60)
textRect3.center= (320,60)


while run:
    screen.fill((255,255,255))

    i=0
    if(start==0):
        while(i<n):

            pygame.draw.rect(screen,blue,(20+12*i,595-h[i],10,h[i]))

            i+=1
    i=0
    if(start==1):
        while(i<n):

            pygame.draw.rect(screen,blue,(20+12*i,595-mer[i],10,mer[i]))

            i+=1
    i=0
    if(start==3):
        while(i<n):

            pygame.draw.rect(screen,blue,(20+12*i,595-ins[i],10,ins[i]))

            i+=1


    pygame.draw.rect(screen,green,(30,35,100,50))
    pygame.draw.rect(screen,red,(150,35,100,50))
    pygame.draw.rect(screen,red,(270,35,100,50))
    screen.blit(textsurf1,textRect1)
    screen.blit(textsurf2,textRect2)
    screen.blit(textsurf3,textRect3)

    pygame.display.update()
    mouse=pygame.mouse.get_pos()
    if (mouse[0]>30 and mouse[0]<130 and mouse[1]>35 and mouse[1]<85):

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen,red,(30,35,100,50))
                pygame.display.update()

                start=0
                while(i<n):

                    pygame.draw.rect(screen,blue,(20+12*i,595-h[i],10,h[i]))

                    i+=1
                #pygame.display.update()

    #while start<1:


    i=0
    if(start==0):
        while(i<n):

            pygame.draw.rect(screen,blue,(20+12*i,595-h[i],10,h[i]))

            i+=1
    mouse=pygame.mouse.get_pos()
    if (mouse[0]>150 and mouse[0]<250 and mouse[1]>35 and mouse[1]<85):


        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                start=1
                mergesort(mer,0,n-1)

    i=0

    if(start==1):
        while(i<n):

            pygame.draw.rect(screen,blue,(20+12*i,595-mer[i],10,mer[i]))

            i+=1

    mouse=pygame.mouse.get_pos()
    if (mouse[0]>270 and mouse[0]<370 and mouse[1]>35 and mouse[1]<85):
        #pygame.draw.rect(screen,lblue,(270,35,100,50))


        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:

                #pygame.display.update()
                start=3
    if(start==3):
        if(p<n):
            q=p+1
            while(q<n):
                if(ins[q]<ins[p]):
                    ins[q],ins[p]=ins[p],ins[q]
                    pygame.draw.rect(screen,blue,(20+12*p,595-ins[p],10,ins[p]))
                    pygame.draw.rect(screen,blue,(20+12*q,595-ins[q],10,ins[q]))
                    pygame.draw.rect(screen,blue,(20+12*(q-1),595-ins[q-1],10,ins[q-1]))
                    pygame.display.update()
                    clock.tick(20)
                    q+=1
                else:
                    pygame.draw.rect(screen,lblue,(20+12*q,595-ins[q],10,ins[q]))
                    if(q>0):
                        pygame.draw.rect(screen,blue,(20+12*(q-1),595-ins[q-1],10,ins[q-1]))
                    pygame.display.update()
                    clock.tick(20)
                    q+=1

            p+=1
    i=0
    if(start==3):
        while(i<n):

            pygame.draw.rect(screen,blue,(20+12*i,595-ins[i],10,ins[i]))

            i+=1





    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
