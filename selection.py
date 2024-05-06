import random
import time

def selection_sort(a):
    for i in range(0,len(a)):
                minimum=a[i]
                pos_min=i
                for j in range(i+1,len(a)):
                    if a[j]<minimum:
                        minimum=a[j]
                        pos_min=j
                if minimum!=a[i]:
                    aux=a[pos_min]
                    a[pos_min]=a[i]
                    a[i]=aux
