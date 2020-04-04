import pygame
#import time
import random
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('visualization')
run=True
blue=(0,0,150)
lblue=(229,204,255)
white=(255,255,255)
h=[]
n=random.randint(20,30)
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
        clock.tick(5)
        if L[i] <= R[j]:
            pygame.draw.rect(screen,white,(40+24*(l+i),0,20,595))
            pygame.draw.rect(screen,white,(40+24*(m+j+1),0,20,595))
            pygame.draw.rect(screen,lblue,(40+24*(l+i),595-arr[l+i],20,arr[l+i]))
            pygame.draw.rect(screen,lblue,(40+24*(m+j+1),595-arr[m+j+1],20,arr[m+j+1]))
            pygame.display.update()
            pygame.time.wait(400)
            #clock.tick(20)
            pygame.draw.rect(screen,blue,(40+24*(l+i),595-arr[l+i],20,arr[l+i]))
            pygame.draw.rect(screen,blue,(40+24*(m+j+1),595-arr[m+j+1],20,arr[m+j+1]))
            pygame.display.update()
            arr[k] = L[i]
            pygame.draw.rect(screen,white,(40+24*(k),0,20,595))
            pygame.draw.rect(screen,blue,(40+24*(k),595-arr[k],20,arr[k]))

            i += 1

            pygame.display.update()
            #clock.tick(20)

        else:
            #rekt=(40+24*(m+j+1),0,20,595)
            pygame.draw.rect(screen,white,(40+24*(k),0,20,595))
            pygame.draw.rect(screen,white,(40+24*(m+j+1),0,20,595))
            pygame.draw.rect(screen,lblue,(40+24*(k),595-arr[k],20,arr[k]))
            pygame.draw.rect(screen,lblue,(40+24*(m+j+1),595-arr[k],20,arr[k]))
            pygame.display.update()
            pygame.time.wait(400)
            #clock.tick(20)
            pygame.draw.rect(screen,blue,(40+24*(m+j+1),595-arr[k],20,arr[k]))
            pygame.draw.rect(screen,blue,(40+24*(m+j+1),595-arr[k],20,arr[k]))
            pygame.display.update()
            arr[k] = R[j]
            pygame.draw.rect(screen,white,(40+24*(k),0,20,595))
            pygame.draw.rect(screen,blue,(40+24*(k),595-arr[k],20,arr[k]))
            j += 1



            pygame.display.update()
            #clock.tick(20)
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        clock.tick(5)
        pygame.draw.rect(screen,white,(40+24*(l+i),0,20,595))
        pygame.draw.rect(screen,lblue,(40+24*(l+i),595-arr[l+i],20,arr[l+i]))

        pygame.display.update()
        pygame.time.wait(400)
        #clock.tick(20)
        pygame.draw.rect(screen,blue,(40+24*(l+i),595-arr[l+i],20,arr[l+i]))
        pygame.display.update()
        arr[k] = L[i]
        pygame.draw.rect(screen,white,(40+24*(k),0,20,595))
        pygame.draw.rect(screen,blue,(40+24*(k),595-arr[k],20,arr[k]))
        i += 1
        pygame.display.update()
        #clock.tick(20)
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        clock.tick(5)
        pygame.draw.rect(screen,white,(40+24*(m+j+1),0,20,595))
        pygame.draw.rect(screen,lblue,(40+24*(j+m+1),595-arr[j+m+1],20,arr[j+m+1]))

        pygame.display.update()
        pygame.time.wait(400)
        #clock.tick(20)
        pygame.draw.rect(screen,blue,(40+24*(m+j+1),595-arr[j+m+1],20,arr[j+m+1]))
        pygame.display.update()
        arr[k] = R[j]
        pygame.draw.rect(screen,white,(40+24*(k),0,20,595))
        pygame.draw.rect(screen,blue,(40+24*(k),595-arr[k],20,arr[k]))
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
#draw.rect(a,b,c,d) where a,b=x,y coordinate of top left
#c=width,d=height
while run:
    screen.fill((255,255,255))
    i=0
    while(i<n):

        pygame.draw.rect(screen,blue,(40+24*i,595-h[i],20,h[i]))

        i+=1

    while(x<1):
        mergesort(h,0,n-1)
        x+=1


#    if(p<n):
#        q=p+1
#            if(h[q]<h[p]):
#
#
#                pygame.draw.rect(screen,blue,(40+24*p,595-h[p],20,h[p]))
#                pygame.draw.rect(screen,blue,(40+24*q,595-h[q],20,h[q]))
#                pygame.draw.rect(screen,blue,(40+24*(q-1),595-h[q-1],20,h[q-1]))
#                pygame.display.update()
#                clock.tick(10)
#                q+=1
#            else:
#                pygame.draw.rect(screen,lblue,(40+24*q,595-h[q],20,h[q]))
#                if(q>0):
#                    pygame.draw.rect(screen,blue,(40+24*(q-1),595-h[q-1],20,h[q-1]))
#                pygame.display.update()
#                clock.tick(10)
#                q+=1

#        p+=1





    #if(k<n):
        #if(k>0):
            #pygame.draw.rect(screen,blue,(40+24*(k-1),595-h[k-1],20,h[k-1]))
        #pygame.draw.rect(screen,lblue,(40+24*k,595-h[k],20,h[k]))
        #k+=1

        #pygame.display.update()
        #clock.tick(5)
        #time.sleep(100)



    #mouse=pygame.mouse.get_pos()
    #print(mouse)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
