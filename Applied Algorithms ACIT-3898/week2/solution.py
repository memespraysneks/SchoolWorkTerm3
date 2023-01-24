def swap(arr, index_a, index_b):
    arr[index_a], arr[index_b] = arr[index_b], arr[index_a]


def selection_sort(arr):
    # clean_size = 0
    # while sorted(arr) != arr:
    #     smallest = min(arr[clean_size:])
    #     swap(arr, arr.index(smallest), clean_size)
    #     clean_size += 1
    # return arr

    
    for j in range(len(arr)):
        smallest = None
        index = None
        for i in range(j, len(arr)):
            if smallest == None:
                smallest = arr[i]
                index = i
            elif smallest > arr[i]:
                smallest = arr[i]
                index = i
        swap(arr, index, j)
    return arr

def insertion_sort(arr):
    clean_size = 0
    for i in range(len(arr)):
        for j in range(0, clean_size):
            if arr[i] < arr[j]:
                swap(arr, i, j)
        clean_size += 1
                
    return arr

def bubble_sort(arr):
    while sorted(arr) != arr:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
    