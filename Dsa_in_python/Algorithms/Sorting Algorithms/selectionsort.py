def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):  
        min_index = i                                          # Assuming first element as the smallest
        
        for j in range(i+1, n):                                # Finding smallest element
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]        # Swaping elements

arr = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input())  
    arr.append(element)

selection_sort(arr)                                            # sorting th array
print("Sorted array:", arr)
