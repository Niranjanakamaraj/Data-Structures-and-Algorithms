def merge_sort(arr):
    if len(arr) <= 1:
        return arr 

    mid = len(arr) // 2                             # Dividing the array into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)                       # Merging the sorted subarrays

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):         # Comparing elements from both halves and merge them in sorted order
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])                         # Appending the remaining elements, if any
    result.extend(right[j:])
    return result
arr = []
n = int(input("Enter number of elements: ")) 

print("Enter the elements:")
for i in range(n):
    element = int(input()) 
    arr.append(element)

sorted_arr = merge_sort(arr)                         # Sorting the array
print("Sorted array:", sorted_arr)
