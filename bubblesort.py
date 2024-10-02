def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False                                         # Tracking if any swap happens in this pass
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]         # swapping
                swapped = True
        
        if not swapped:
            break
arr = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input())  
    arr.append(element)

bubble_sort(arr)                                               # sorting array
print("Sorted array:", arr)
