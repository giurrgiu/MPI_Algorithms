import random
import time

def insertion_sort(a):
    for i in range(1,len(a)):
                pos=i-1
                aux=a[i]
                while pos>=0:
                    if aux<a[pos]:
                        a[pos+1]=a[pos]
                    else:
                        break
                    pos-=1
                a[pos+1]=aux



