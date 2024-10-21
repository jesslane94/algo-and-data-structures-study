def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i, j, iterator_main = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[iterator_main] = left[i]
                i += 1
            else:
                arr[iterator_main] = right[j]
                j += 1
            iterator_main += 1
        
        while i < len(left):
            arr[iterator_main] = left[i]
            i += 1
            iterator_main += 1
        while j < len(right):
            arr[iterator_main] = right[j]
            j += 1
            iterator_main += 1


my_array = [9,4,6,2,10]
mergesort(my_array)
print(my_array)