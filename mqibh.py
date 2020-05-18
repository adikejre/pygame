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
whit=(255,255,255)
skin=(255,204,205)
red=(255,255,153)
dark=(255,0,0)
green=(153,255,204)
dg=(0,255,0)
black=(0,0,0)
brown=(100,100,100)
h=[]

i=0
k=0
m=0
p=0
q=0
def merge(arr,l,m,r):

    n1 = m - l + 1
    n2 = r- m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2 :

        clock.tick(15)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                return
        if L[i] <= R[j]:

            pygame.draw.rect(screen,skin,(20+12*(l+i),150,10,595))
            pygame.draw.rect(screen,skin,(20+12*(m+j+1),250,10,595))
            pygame.draw.rect(screen,lblue,(20+12*(l+i),595-arr[l+i],10,arr[l+i]))
            pygame.draw.rect(screen,lblue,(20+12*(m+j+1),595-arr[m+j+1],10,arr[m+j+1]))
            pygame.display.update()
            pygame.time.wait(70)
            #clock.tick(20)
            pygame.draw.rect(screen,blue,(20+12*(l+i),595-arr[l+i],10,arr[l+i]))
            pygame.draw.rect(screen,blue,(20+12*(m+j+1),595-arr[m+j+1],10,arr[m+j+1]))
            pygame.display.update()
            arr[k] = L[i]
            pygame.draw.rect(screen,skin,(20+12*(k),150,10,595))
            pygame.draw.rect(screen,blue,(20+12*(k),595-arr[k],10,arr[k]))

            i += 1

            pygame.display.update()
            #clock.tick(20)

        else:
            #rekt=(40+24*(m+j+1),0,20,595)
            pygame.draw.rect(screen,skin,(20+12*(k),150,10,595))
            pygame.draw.rect(screen,skin,(20+12*(m+j+1),150,10,595))
            pygame.draw.rect(screen,lblue,(20+12*(k),595-arr[k],10,arr[k]))
            pygame.draw.rect(screen,lblue,(20+12*(m+j+1),595-arr[k],10,arr[k]))
            pygame.display.update()
            pygame.time.wait(70)
            #clock.tick(20)
            pygame.draw.rect(screen,blue,(20+12*(m+j+1),595-arr[k],10,arr[k]))
            pygame.draw.rect(screen,blue,(20+12*(m+j+1),595-arr[k],10,arr[k]))
            pygame.display.update()
            arr[k] = R[j]
            pygame.draw.rect(screen,skin,(20+12*(k),150,10,595))
            pygame.draw.rect(screen,blue,(20+12*(k),595-arr[k],10,arr[k]))
            j += 1



            pygame.display.update()
            #clock.tick(20)
        k += 1

    while i < n1:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                return
        pygame.draw.rect(screen,skin,(20+12*(l+i),150,10,595))
        pygame.draw.rect(screen,lblue,(20+12*(l+i),595-arr[l+i],10,arr[l+i]))

        pygame.display.update()
        pygame.time.wait(100)
        #clock.tick(20)
        pygame.draw.rect(screen,blue,(20+12*(l+i),595-arr[l+i],10,arr[l+i]))
        pygame.display.update()
        arr[k] = L[i]
        pygame.draw.rect(screen,skin,(20+12*(k),150,10,595))
        pygame.draw.rect(screen,blue,(20+12*(k),595-arr[k],10,arr[k]))
        i += 1
        pygame.display.update()
        #clock.tick(20)
        k += 1

    while j < n2:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                return
        pygame.draw.rect(screen,skin,(20+12*(m+j+1),150,10,595))
        pygame.draw.rect(screen,lblue,(20+12*(j+m+1),595-arr[j+m+1],10,arr[j+m+1]))

        pygame.display.update()
        pygame.time.wait(100)
        #clock.tick(20)
        pygame.draw.rect(screen,blue,(20+12*(m+j+1),595-arr[j+m+1],10,arr[j+m+1]))
        pygame.display.update()
        arr[k] = R[j]
        pygame.draw.rect(screen,skin,(20+12*(k),150,10,595))
        pygame.draw.rect(screen,blue,(20+12*(k),595-arr[k],10,arr[k]))
        j += 1

        pygame.display.update()
        #clock.tick(20)
        k+=1

#merge ends
def mergesort(ar,l,r):

    if l<r:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                return
        m=(l+r)//2
        mergesort(ar,l,m)
        mergesort(ar,m+1,r)
        merge(ar,l,m,r)


def partition(arr,low,high):
    clock.tick(20)
    pivot=arr[high]

    pygame.draw.rect(screen,dark,(20+12*(high),595-arr[high],10,arr[high]))
    pygame.time.wait(200)
    pygame.display.update()
    pygame.time.wait(500)
    pygame.draw.rect(screen,blue,(20+12*(high),595-arr[high],10,arr[high]))
    pygame.display.update()
    i=low-1
    j=low
    while(j<=high):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                return
        pygame.draw.rect(screen,lblue,(20+12*(j),595-arr[j],10,arr[j]))
        #pygame.draw.rect(screen,lblue,(20+12*(high),595-pivot,10,pivot))
        pygame.display.update()
        pygame.time.wait(50)
        pygame.draw.rect(screen,blue,(20+12*(j),595-arr[j],10,arr[j]))
        #pygame.draw.rect(screen,blue,(20+12*(high),595-pivot,10,pivot))
        pygame.display.update()
        if(arr[j]<pivot):
            i+=1
            pygame.draw.rect(screen,lblue,(20+12*(i),595-arr[i],10,arr[i]))
            pygame.draw.rect(screen,lblue,(20+12*(j),595-arr[j],10,arr[j]))
            pygame.display.update()
            pygame.time.wait(50)
            pygame.draw.rect(screen,blue,(20+12*(i),595-arr[i],10,arr[i]))
            pygame.draw.rect(screen,blue,(20+12*(j),595-arr[j],10,arr[j]))
            pygame.display.update()
            arr[i],arr[j]=arr[j],arr[i]
            pygame.draw.rect(screen,skin,(20+12*(i),150,10,595))
            pygame.display.update()
            pygame.draw.rect(screen,blue,(20+12*(i),595-arr[i],10,arr[i]))
            pygame.draw.rect(screen,skin,(20+12*(j),150,10,595))
            pygame.display.update()
            pygame.draw.rect(screen,blue,(20+12*(j),595-arr[j],10,arr[j]))
            pygame.display.update()
        j+=1

    arr[i+1],arr[high]=arr[high],arr[i+1]
    pygame.draw.rect(screen,skin,(20+12*(i+1),150,10,595))
    pygame.display.update()
    pygame.draw.rect(screen,blue,(20+12*(i+1),595-arr[i+1],10,arr[i+1]))
    pygame.draw.rect(screen,skin,(20+12*(high),150,10,595))
    pygame.display.update()
    pygame.draw.rect(screen,blue,(20+12*(high),595-arr[high],10,arr[high]))
    pygame.display.update()
    pygame.draw.rect(screen,dg,(20+12*(i+1),595-arr[i+1],10,arr[i+1]))

    #pygame.display.update()
    #pygame.time.wait(500)
    #pygame.draw.rect(screen,blue,(20+12*(i+1),595-arr[i+1],10,arr[i+1]))
    pygame.display.update()
    pygame.time.wait(200)
    return i+1

def quicksort(arr,low,high):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            return
    if (low<high):
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)


def bubble(arr,n):

    i=0
    while(i<n):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                return
        j=0
        while(j<n-i-1):
            pygame.draw.rect(screen,lblue,(20+12*(j),595-arr[j],10,arr[j]))
            pygame.draw.rect(screen,lblue,(20+12*(j+1),595-arr[j+1],10,arr[j+1]))
            pygame.display.update()
            pygame.time.wait(30)
            pygame.draw.rect(screen,blue,(20+12*(j),595-arr[j],10,arr[j]))
            pygame.draw.rect(screen,blue,(20+12*(j+1),595-arr[j+1],10,arr[j+1]))
            pygame.display.update()
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                pygame.draw.rect(screen,skin,(20+12*(j),150,10,595))
                pygame.draw.rect(screen,blue,(20+12*(j),595-arr[j],10,arr[j]))
                pygame.draw.rect(screen,skin,(20+12*(j+1),150,10,595))
                pygame.draw.rect(screen,blue,(20+12*(j+1),595-arr[j+1],10,arr[j+1]))
                pygame.display.update()

            j+=1
        i+=1

def heapify(arr,n,i):
    clock.tick(20)
    largest=i
    l=2*i+1
    r=2*i+2
    if(l<n):
        pygame.draw.rect(screen,lblue,(20+12*(l),595-arr[l],10,arr[l]))
        pygame.draw.rect(screen,lblue,(20+12*(largest),595-arr[largest],10,arr[largest]))
        pygame.display.update()
        pygame.time.wait(60)
        pygame.draw.rect(screen,blue,(20+12*(l),595-arr[l],10,arr[l]))
        pygame.draw.rect(screen,blue,(20+12*(largest),595-arr[largest],10,arr[largest]))
        pygame.display.update()
        if(arr[l]>arr[largest]):
            largest=l
    if(r<n):
        pygame.draw.rect(screen,lblue,(20+12*(r),595-arr[r],10,arr[r]))
        pygame.draw.rect(screen,lblue,(20+12*(largest),595-arr[largest],10,arr[largest]))
        pygame.display.update()
        pygame.time.wait(60)
        pygame.draw.rect(screen,blue,(20+12*(r),595-arr[r],10,arr[r]))
        pygame.draw.rect(screen,blue,(20+12*(largest),595-arr[largest],10,arr[largest]))
        pygame.display.update()
        if(arr[r]>arr[largest]):
            largest=r
    if(largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        pygame.draw.rect(screen,skin,(20+12*(i),150,10,595))
        pygame.draw.rect(screen,blue,(20+12*(i),595-arr[i],10,arr[i]))
        pygame.draw.rect(screen,skin,(20+12*(largest),150,10,595))
        pygame.draw.rect(screen,blue,(20+12*(largest),595-arr[largest],10,arr[largest]))
        pygame.display.update()
        heapify(arr,n,largest)

def heapsort(arr,n):
    clock.tick(20)
    i=(n//2)-1
    while(i>=0):
        heapify(arr,n,i)
        i-=1

    i=n-1
    while(i>0):
        arr[0],arr[i]=arr[i],arr[0]
        pygame.draw.rect(screen,skin,(20+12*(i),150,10,595))
        pygame.draw.rect(screen,blue,(20+12*(i),595-arr[i],10,arr[i]))
        pygame.draw.rect(screen,skin,(20+12*(0),150,10,595))
        pygame.draw.rect(screen,blue,(20+12*(0),595-arr[0],10,arr[0]))
        pygame.display.update()
        heapify(arr,i,0)
        i-=1
#end of heapsort


z=0
x=0
mm=0
start=-1
mer=[]
ins=[]
par=[]
bub=[]
hep=[]

#draw.rect(a,b,c,d) where a,b=x,y coordinate of top left
#c=width,d=height
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface, textsurface.get_rect()



font = pygame.font.Font('freesansbold.ttf', 15)
textsurf1,textRect1= text_objects("Start/Reset",font)
textsurf2,textRect2= text_objects("Merge Sort",font)
textsurf3,textRect3= text_objects("Insertion Sort",font)
textsurf4,textRect4= text_objects("Quick Sort",font)
textsurf5,textRect5= text_objects("Bubble Sort",font)
textsurf6,textRect6= text_objects("Heap Sort",font)
textRect1.center= (80,60)
textRect2.center= (200,60)
textRect3.center= (320,60)
textRect4.center=(442,60)
textRect5.center=(560,60)
textRect6.center=(680,60)
while run:
    screen.fill((255,204,205))

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
    i=0

    if(start==4):
        while(i<n):
            pygame.draw.rect(screen,blue,(20+12*i,595-par[i],10,par[i]))

            i+=1
    i=0

    if(start==5):
        while(i<n):
            pygame.draw.rect(screen,blue,(20+12*i,595-bub[i],10,bub[i]))

            i+=1
    i=0
    if(start==6):
        while(i<n):
            pygame.draw.rect(screen,blue,(20+12*i,595-hep[i],10,hep[i]))

            i+=1


    pygame.draw.rect(screen,green,(30,35,100,50))
    pygame.draw.rect(screen,red,(150,35,100,50))
    pygame.draw.rect(screen,red,(270,35,100,50))
    pygame.draw.rect(screen,red,(390,35,100,50))
    pygame.draw.rect(screen,red,(510,35,100,50))
    pygame.draw.rect(screen,red,(630,35,100,50))
    screen.blit(textsurf1,textRect1)
    screen.blit(textsurf2,textRect2)
    screen.blit(textsurf3,textRect3)
    screen.blit(textsurf4,textRect4)
    screen.blit(textsurf5,textRect5)
    screen.blit(textsurf6,textRect6)

    pygame.display.update()
    mouse=pygame.mouse.get_pos()
    if (mouse[0]>30 and mouse[0]<130 and mouse[1]>35 and mouse[1]<85):

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:

                start=0
                h=[]
                mer=[]
                ins=[]
                par=[]
                bub=[]
                hep=[]
                n=random.randint(60,77)
                i=0
                while(i<n):
                    h.append(random.randint(20,400))
                    i+=1
                mm=0
                while(mm<n) :
                    mer.append(h[mm])
                    ins.append(h[mm])
                    par.append(h[mm])
                    bub.append(h[mm])
                    hep.append(h[mm])
                    mm+=1
                while(i<n):

                    pygame.draw.rect(screen,blue,(20+12*i,595-h[i],10,h[i]))

                    i+=1
                pygame.display.update()

    i=0
    if(start==0):
        while(i<n):

            pygame.draw.rect(screen,blue,(20+12*i,595-h[i],10,h[i]))

            i+=1
    mouse=pygame.mouse.get_pos()
    if (mouse[0]>150 and mouse[0]<250 and mouse[1]>35 and mouse[1]<85):


        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                f=0
                while(f<n):
                    pygame.draw.rect(screen,skin,(20+12*f,150,10,595))
                    pygame.draw.rect(screen,blue,(20+12*f,595-h[f],10,h[f]))
                    f+=1

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
    mouse=pygame.mouse.get_pos()
    if (mouse[0]>390 and mouse[0]<490 and mouse[1]>35 and mouse[1]<85):


        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                start=4
                ff=0
                while(ff<n):
                    pygame.draw.rect(screen,skin,(20+12*ff,150,10,595))
                    pygame.draw.rect(screen,blue,(20+12*ff,595-h[ff],10,h[ff]))
                    ff+=1


                quicksort(par,0,n-1)

    i=0
    if(start==4):
        while (i<n):

            pygame.draw.rect(screen,blue,(20+12*i,595-par[i],10,par[i]))

            i+=1

    if (mouse[0]>510 and mouse[0]<610 and mouse[1]>35 and mouse[1]<85):


        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                start=5
                f2=0
                while(f2<n):
                    pygame.draw.rect(screen,skin,(20+12*f2,150,10,595))
                    pygame.draw.rect(screen,blue,(20+12*f2,595-h[f2],10,h[f2]))
                    f2+=1
                bubble(bub,n)
    i=0
    if(start==5):
        while(i<n):
            pygame.draw.rect(screen,blue,(20+12*i,595-bub[i],10,bub[i]))

            i+=1

    if (mouse[0]>630 and mouse[0]<730 and mouse[1]>35 and mouse[1]<85):


        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                start=6
                f3=0
                while(f3<n):
                    pygame.draw.rect(screen,skin,(20+12*f3,150,10,595))
                    pygame.draw.rect(screen,blue,(20+12*f3,595-h[f3],10,h[f3]))
                    f3+=1
                heapsort(hep,n)
    i=0
    if(start==6):
        while(i<n):
            pygame.draw.rect(screen,blue,(20+12*i,595-hep[i],10,hep[i]))

            i+=1



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
