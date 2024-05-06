import random
import time

def merge(list_a,list_b,arr):
    i=j=k=0
    while (i<len(list_a) and j<len(list_b)):
        if list_a[i]<list_b[j]:
            arr[k]=list_a[i]
            i+=1
        else:
            arr[k]=list_b[j]
            j+=1
        k+=1
        
    while (i<len(list_a)):
        arr[k]=list_a[i]
        i+=1
        k+=1
    while(j<len(list_b)):
        arr[k]=list_b[j]
        k+=1
        j+=1


def merge_sort(arr):
    if len(arr)<=1:
        return
    middle=len(arr)//2
    left_arr=[]
    right_arr=[]
    for i in range(0,len(arr)):
        if i<middle:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])
    merge_sort(left_arr)
    merge_sort(right_arr)
    merge(left_arr,right_arr,arr)




