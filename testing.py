import random
import time
import copy

#For QuickSort to not crash due to bad partitioning (exceeds a number of recursion calls)
from sys import setrecursionlimit
setrecursionlimit(100000)

#Sorting Algorithms
from bubble import bubble_sort
from insertion import insertion_sort
from selection import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from counting_sort import counting_sort
from radix_sort import radix_sort

#Add the array sizes you want to sort
sizes=[10,50,100,500,100]

#Add the ranges you want the integers to be picked from
ranges=[100000000]

def tests():
    for size in sizes:
        array=[]
        for rang in ranges:
            array=[]
            for j in range(0,size):
                array.append(random.randint(0,rang))
            print(f"\nArray generated of length {len(array)} and it's elements are in the range of [{0},{rang}]")
            # Call the algorithms you want the tests the be done on:
            bubble(array)
            insertion(array)
            selection(array)
            merge_(array)
            quick_(array)
            counting_(array)
            radix_(array)

            

def merge_(array):
    print("Merge Sort!")
    copy_array=copy.deepcopy(array)
    start=time.time()
    merge_sort(copy_array)
    end=time.time()
    if(copy_array==sorted(copy_array)):
        print(f"It took {end-start} seconds to sort")

def quick_(array):
    print("Quick Sort!")
    copy_array=copy.deepcopy(array)
    start=time.time()
    quick_sort(copy_array,0,len(copy_array)-1)
    end=time.time()
    if(copy_array==sorted(copy_array)):
        print(f"It took {end-start} seconds to sort")

def counting_(array):
    print("Counting Sort!")
    copy_array=copy.deepcopy(array)
    start=time.time()
    copy_array=counting_sort(copy_array)
    end=time.time()
    if(copy_array==sorted(copy_array)):
        print(f"It took {end-start} seconds to sort")


def radix_(array):
    print("Radix Sort!")
    copy_array=copy.deepcopy(array)
    start=time.time()
    radix_sort(copy_array)
    end=time.time()
    if(copy_array==sorted(copy_array)):
        print(f"It took {end-start} seconds to sort")

def bubble(array):
    print("Bubble Sort!")
    copy_array=copy.deepcopy(array)
    start=time.time()
    bubble_sort(copy_array)
    end=time.time()
    if(copy_array==sorted(copy_array)):
        print(f"It took {end-start} seconds to sort")

def insertion(array):
    print("Insertion Sort!")
    copy_array=copy.deepcopy(array)
    start=time.time()
    insertion_sort(copy_array)
    end=time.time()
    if(copy_array==sorted(copy_array)):
        print(f"It took {end-start} seconds to sort")

def selection(array):
    print("Selection Sort!")
    copy_array=copy.deepcopy(array)
    start=time.time()
    selection_sort(copy_array)
    end=time.time()
    if(copy_array==sorted(copy_array)):
        print(f"It took {end-start} seconds to sort")

#Call tests() function to do the tests.

tests()
