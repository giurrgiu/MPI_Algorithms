import random
import time
def quick_sort(array,start,end):
    if start<end:    
        pivot=partition(array,start,end)
        quick_sort(array,start,pivot-1)
        quick_sort(array,pivot+1,end)

def partition(array,start,end):     
    pivot=array[end]
    i=start
    for j in range(start,end):
        if array[j]<=pivot:
            aux=array[i]
            array[i]=array[j]
            array[j]=aux
            i+=1
    aux=array[i]
    array[i]=array[end]
    array[end]=aux
    return i
