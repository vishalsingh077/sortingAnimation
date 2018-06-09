import os
import pygame
import sys
import random
from pygame import *


pygame.init()

scr_size = (width,height) = (1000,700)

fps = 20;

back =(0,0,0)
white = (255,255,255)
green = (0,255,0)

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("quickSort")

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

def quickSort(arr,low,high):
    if low<high:
        pi = Partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

def Partition(arr,low,high):
    pivot = arr[high]
    i = low -1
    for j in range(low,high,1):
           if arr[j] <= pivot:
            i = i +1
            arr[i],arr[j] = arr[j],arr[i]
            dispArray(arr)
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1   

def dispArray(arr):
    screen.fill(white)
    for i in range(n):
        pygame.draw.rect(screen,green ,[80+i*2*barWidth,height-100,barWidth,-arr[i]])
    pygame.display.update()
    #clock.tick(fps)

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
        quickSort(arr,0,n-1)
    else:
        dispArray(arr)
pygame.quit()
quit()
