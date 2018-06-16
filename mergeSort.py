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
pygame.display.set_caption("mergeSort")

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

def mergeSort(arr,low,high):
    if low < high:
        mid = int((low +high)/2)
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    n1 = mid-low +1
    n2 = high - mid
    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = arr[low+i]
    for j in range(n2):
        R[j] = arr[mid+1+j]

    i = 0
    j = 0
    k = low
    while i<n1 and j<n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i = i+1
        else:
            arr[k] = R[j]
            j = j+1
        k = k+1
        dispArray(arr)
    while i<n1:
        arr[k] = L[i]
        i = i+1
        k = k+1
        dispArray(arr)
    while j<n2:
        arr[k] = R[j]
        j = j+1
        k = k+1
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
        mergeSort(arr,0,n-1)
    else:
        dispArray(arr)
pygame.quit()
quit()
