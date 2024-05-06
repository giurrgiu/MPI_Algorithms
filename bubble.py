import random
import time

def bubble_sort(a):
    for i in range(0,len(a)-1):
        swapped=0
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                aux=a[j+1]
                a[j+1]=a[j]
                a[j]=aux
                swapped=1
        if swapped==0:
            break


