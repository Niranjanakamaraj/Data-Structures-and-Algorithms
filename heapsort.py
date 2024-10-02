def heapify(arr, n, i):
    largest = i                                         # Initializing largest as root
    left = 2 * i + 1                                    # Left child
    right = 2 * i + 2                                   # Right child

    if left < n and arr[left] > arr[largest]:           # checking if the left child is larger than the root
        largest = left
    if right < n and arr[right] > arr[largest]:         # checking the right child is larger than the largest so far
        largest = right
    if largest != i:                                    # checking if the largest is not the root to swap it
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, largest)                        # Heapifying the affected subtree

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):                 # Building a max heap
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]                 # Moving the current root to the end
        heapify(arr, i, 0)
arr = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input()) 
    arr.append(element)

heap_sort(arr)                                         # Sorting the array
print("Sorted array:", arr)
