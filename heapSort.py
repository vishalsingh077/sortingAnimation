import os
import pygame
import sys
import random
from pygame import *


pygame.init()

scr_size = (width,height) = (1000,700)

fps = 40;

back =(0,0,0)
white = (255,255,255)
green = (0,255,0)

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("heapSort")

### variables
n=200
start =1
end = 500
barWidth = 2

### function definitions

def randArray(n ,start ,end):
    arr = []
    for i in range(n):
        arr.append(random.randint(start,end))
    return arr

def heapify(arr,n,ind):
    largest = ind
    left_child = 2*ind + 1
    right_child = 2*ind + 2
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    if largest!= ind:
        arr[largest],arr[ind] = arr[ind],arr[largest]
        heapify(arr,n,largest)
    dispArray(arr)

def heapSort(arr,n):
    ind = int((n/2) -1)
    while ind >= 0:
        heapify(arr,n,ind)
        ind = ind - 1
    i = n-1
    while i >= 0:
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
        i = i-1
                 
def dispArray(arr):
    screen.fill(white)
    for i in range(n):
        pygame.draw.rect(screen,green ,[80+i*2*barWidth,height-100,barWidth,-arr[i]])
    pygame.display.update()
    clock.tick(fps)

### creating random array
    
arr = randArray(n,start,end)
sortedArray = sorted(arr)

### loop
Exit = False

while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True

    if sortedArray != arr:
        heapSort(arr,n)
    else:
        dispArray(arr)
pygame.quit()
quit()
