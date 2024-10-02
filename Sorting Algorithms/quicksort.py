def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    pivot = arr[len(arr) // 2]                           # Choosing the middle element as the pivot
    left = [x for x in arr if x < pivot]                 # Elements less than pivot
    middle = [x for x in arr if x == pivot]              # Elements equal to pivot
    right = [x for x in arr if x > pivot]                # Elements greater than pivot
    
    return quick_sort(left) + middle + quick_sort(right) # recursively sorting and combining

arr = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input())  
    arr.append(element)

sorted_arr = quick_sort(arr)                              # sorting the array
print("Sorted array:", sorted_arr)
