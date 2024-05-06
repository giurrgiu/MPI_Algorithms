import random
import time
def counting_sort(array,a):
    sorted_array=[0]*len(array)

    count_array=[0]*10
    for i in range(0,len(array)):
        count_array[(array[i]//a)%10]+=1

    for i in range(1,len(count_array)):
        count_array[i]=count_array[i]+count_array[i-1]

    for i in range(len(array)-1,-1,-1):
        sorted_array[count_array[(array[i]//a)%10]-1]=array[i]
        count_array[(array[i]//a)%10]-=1
    
    for i in range(0,len(array)):
        array[i]=sorted_array[i]

def radix_sort(array):
    maximum=0
    for i in range(0,len(array)):
        if array[i]>maximum:
            maximum=array[i]
    number=1

    while maximum/number>=1:
        counting_sort(array,number)
        number*=10

