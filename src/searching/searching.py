def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"{True}, Found {target}")
            return i
    print(f"{False}, {target} Not Found")    
    return -1   # not found

linear_search([1, 2, 3, 4, 5], 6)
linear_search([1, 2, 3, 4, 5], 4)


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            print(f"{False}, {target} Not Found")   
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print(f"{False}, {target} Not Found")   
    return -1  # not found
binary_search([1, 2, 3, 4, 5], 6)
binary_search([1, 2, 3, 4, 5], 4)