def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]                                 # Element to be placed at the correct position
        j = i - 1
        
        while j >= 0 and arr[j] > key:               # Moving elements if greater than key to one position ahead
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key                             # Placing key at its correct position

arr = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input()) 
    arr.append(element)

insertion_sort(arr)                                  # sorting the array
print("Sorted array:", arr)
