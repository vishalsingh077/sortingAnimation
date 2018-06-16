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
pygame.display.set_caption("bubbleSort")

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

def bubbleSort(arr):
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swapped = True
                dispArray(arr)
        if swapped == False:
            break
        
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
        bubbleSort(arr)
    else:
        dispArray(arr)
pygame.quit()
quit()
