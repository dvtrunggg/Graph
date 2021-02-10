import sys
list = [3,7,2,5,-7,32,-9,0]
print(list)

def SequentialSearch(list, number):
    #found = False
    for i in range(len(list)): #and not found:  #phủ định found = True
        if list[i] == number:
            print(number, 'is list , position: ', i) 
   

# use recursive  
def BinarySearch(a, number, left, right): # a is list sorted
    if right >= left:
        mid = left + (right - left) // 2
        if a[mid] == number:
            return mid
        elif a[mid] > number :
            return BinarySearch(a,number,left,mid - 1)
        else:                   #a[mid] < number
            return BinarySearch(a,number, mid + 1, right)
    else:
        return -1

#use iterative
def bSearch(a, l, r, x):  #BinarySearch
    while r >= l:
        mid = l + (r - l) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            r = mid - 1
        else:           #(a[mid < x)
            l = mid + 1
    return -1
def SelectionSort(list):
    for i in range(0 , len(list)):   #ko khai bao=>start = 0, step = 1, stop = len(list
        min = i                     # ko cần 0 cũng dc: range(len(list))
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j           # update lại giá trị của min
        list[i], list [min] = list[min], list[i] #swap
 
def Heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2  
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
        # Heapify the root. 
        Heapify(arr, n, largest) 
        
def HeapSort(arr): 
    n = len(arr)  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        Heapify(arr, n, i) 
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        Heapify(arr, i, 0) 

def mergeSort(integers):
    if len(integers) > 1:
        mid = len(integers) // 2
        left = integers[:mid]
        right = integers[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                integers[k] = left[i]
                i += 1
            else:
                integers[k] = right[j]
                j += 1

            k += 1
        while i < len(left):
            integers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            integers[k] = right[j]
            j += 1
            k += 1

    return integers


def counting_sort(A, r, k):
    t = []
    for i in range(0, k+1):
        t.append(0)
    for i in range(0, len(r)):
        t[r[i]] += 1
    for i in range(1, k+1):
        t[i] = t[i-1] + t[i]
    f = []
    for i in range(0, len(r)):
        f.append(0)
    for i in range(len(r)-1, -1, -1):
        if t[r[i]] != 0:
           f[t[r[i]]-1] = A[i]
        t[r[i]] -= 1
    return f
        

def radixSort(array):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]
        for  i in array:
            tmp = i / placement
            buckets[int(tmp % RADIX)].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1
        placement *= RADIX
  
  
def partition(arr,low,high):
    pindex = low         
    pivot = arr[high]     
 
    for j in range(low , high):
 
        if   arr[j] <= pivot:
            arr[pindex],arr[j] = arr[j],arr[pindex]
            pindex = pindex + 1
 
    arr[pindex],arr[high] = arr[high],arr[pindex]
    return (pindex)

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 



'''
print('SequentialSearch:')
SequentialSearch(list,-7)

print('BinarySearch:')
arr = sorted(list)
#check = BinarySearch(arr, 7, 0, len(list)-1)
check = bSearch(arr, 0, len(list)-1, 7)
if check != -1:
    print ('Element is present at index: ',check  )
else:
    print('Number is not present in list!')
    

SelectionSort(list)
print('Selection Sort: ', list)
'''
#HeapSort(list)
#print('Heapsort: ', list)
#mergeSort(list)
#print('MergeSort: ', list)
#radixSort(list)
#print('RadixSort: ', list)
#n = len(list) - 1
#quickSort(list,0,n)
#print('QuickSort: ', list)

