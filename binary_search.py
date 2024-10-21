# O(log n) runtime, O(1) space
# array must be sorted

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
        
    while left <= right:
        mid = (left + right)//2
        
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return False


def binary_search_recursive(arr, lo, hi, x):
    if hi >= lo:
        mid = (hi + lo) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            binary_search_recursive(arr, lo, mid - 1, x)
        else:
            binary_search_recursive(arr, mid + 1, hi, x)
    else:
        return False


my_array = [1,2,3,4,5]
x = 2
found = binary_search(my_array, x)
rec_result = binary_search_recursive(my_array, 0, len(my_array) - 1, x)
print(found, "and", rec_result)