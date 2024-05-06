import random
import time
def counting_sort(array):
    maximum=0
    sorted_array=[0]*len(array)
    for i in range(0,len(array)):       
        if array[i]>maximum:
            maximum=array[i]

    count_array=[0]*(maximum+1)
    
    for i in range(0,len(array)):
        count_array[array[i]]+=1

    for i in range(1,len(count_array)):
        count_array[i]=count_array[i]+count_array[i-1]

    for i in range(len(sorted_array)-1,-1,-1):
        sorted_array[count_array[array[i]]-1]=array[i]
        count_array[array[i]]-=1
    return sorted_array
