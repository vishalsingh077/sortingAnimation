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
pygame.display.set_caption("insertionSort")

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

def insertionSort(arr):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                dispArray(arr)
            else:
                break
            j = j-1
        arr[j+1] = key
        dispArray(arr)
                
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
        insertionSort(arr)
    else:
        dispArray(arr)
pygame.quit()
quit()
