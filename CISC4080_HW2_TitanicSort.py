# Anton Karabushin
# CISC 4080: Wenqi Wei
# Homework 2
# Implement Merge sort, Bubble sort, Insertion sort, Selection sort and Quicksort on age dataset

import pandas as pd
import numpy as np
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

ages = list(train_data['Age']) + list(test_data['Age'])

ages = [x for x in ages if x == x]

def merge(ages, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = ages[left + i]
    for j in range(n2):
        R[j] = ages[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Merge the temp arrays back into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            ages[k] = L[i]
            i += 1
        else:
            ages[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        ages[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        ages[k] = R[j]
        j += 1
        k += 1

def mergeSort(ages, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(ages, left, mid)
        mergeSort(ages, mid + 1, right)
        merge(ages, left, mid, right)

def bubbleSort(ages):
    n = len(ages)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element.
            if ages[j] > ages[j+1]:
                ages[j], ages[j+1] = ages[j+1], ages[j]
                swapped = True
        if (swapped == False):
            break

def insertionSort(ages):
    for i in range(1, len(ages)):
        key = ages[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key 
        # to one position ahead of their current position.
        while j >= 0 and key < ages[j]:
            ages[j + 1] = ages[j]
            j -= 1
        ages[j + 1] = key

def selectionSort(ages):
    n = len(ages)
    for i in range(n - 1):
      
        # Assume the current position holds the minimum element
        min_idx = i
        
        # Find the actual minimum:
        for j in range(i + 1, n):
            if ages[j] < ages[min_idx]:
                min_idx = j
        
        # If a new minimum is found, swap it with the element at index i
        if min_idx != i:
            ages[i], ages[min_idx] = ages[min_idx], ages[i]

def partition(ages, low, high):
    
    # Choose the pivot
    pivot = ages[high]
    i = low - 1
    
    # Move all smaller elements to the left side
    for j in range(low, high):
        if ages[j] < pivot:
            i += 1
            swap(ages, i, j)
    
    # Move pivot after smaller elements and return its position
    swap(ages, i + 1, high)
    return i + 1

def swap(ages, i, j):
    ages[i], ages[j] = ages[j], ages[i]

def quickSort(ages, low, high):
    if low < high:
        pivIndex = partition(ages, low, high)
        
        # Recursive calls for smaller elements, then larger
        quickSort(ages, low, pivIndex - 1)
        quickSort(ages, pivIndex + 1, high)

def print_list(ages):
    for i in ages:
        print(i, end=" ")
    print()

# main()
print("Given array is")
print_list(ages)

while(True):
    print("\nEnter the letter according to the sorting type would you like to perform:", end="")
    print("\n1. M (Merge Sort)\n2. B (Bubble Sort)\n3. I (Insertion Sort)\n4. S (Selection Sort)\n5. Q (Quicksort)")
    EntryType = input()

    if EntryType in ["m","M"]:
        mergeSort(ages, 0, len(ages) - 1)
        break
    elif EntryType in ["b","B"]:
        bubbleSort(ages)
        break
    elif EntryType in ["i","I"]:
        insertionSort(ages)
        break
    elif EntryType in ["s","S"]:
        selectionSort(ages)
        break
    elif EntryType in ["q","Q"]:
        quickSort(ages, 0, len(ages) - 1)
        break
    else:
       print('\nInvalid input; try again.')
       continue

print("\nSorted array is")
print_list(ages)