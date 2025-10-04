def binary_search(arr, target):
    if len(arr) == 0:                                               # Check for empty array
        return -1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid                                               # Target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1                                                        # Target not found
                                                                     
def main():                                                          # Main function                
    size = input("Enter the size of the array: ")                    # Getting input from the user
    while size == '':                                                # Check if input is empty
        print("Input cannot be empty. Please enter a valid number.")
        size = input("Enter the size of the array: ")                # Re-prompt until valid input
    size = int(size)                                                 # Convert to integer assuming it's valid
    
    arr = []                                                         # Continue with your logic to fill the array
    print("Enter the sorted array:")
    for i in range(size):
        element = int(input(f"Element {i + 1}: "))
        arr.append(element)
    target = int(input("Enter search element : "))

    result = binary_search(arr, target)                              # Performing binary search
    if result != -1:
        print(f"Binary Search: Target found at index {result}")
    else:
        print("Binary Search: Target not found in the array")


if __name__ == "__main__":
    main()

