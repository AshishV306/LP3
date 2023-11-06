def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i = i + 1
        while j > left and arr[j] >= pivot:
            j = j - 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:                
        arr[i], arr[right] = arr[right], arr[i]

    return i

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

arr = [22, 11, 88, 66, 55, 77, 33, 44, -4, 0]
quicksort(arr, 0, len(arr)-1)
print(arr)


 # Randomly select a pivot and swap it with the last element
        # random_pivot = random.randint(left, right)
        # arr[random_pivot], arr[right] = arr[right], arr[random_pivot]

 # Choose the pivot using a deterministic strategy (e.g., median-of-three)
    # pivot_index = left + (right - left) // 2
    # pivot = arr[pivot_index]
    
    # i = left
    # j = right

    # while i <= j:
    #     while arr[i] < pivot:
    #         i += 1
    #     while arr[j] > pivot:
    #         j -= 1
    #     if i <= j:
    #         arr[i], arr[j] = arr[j], arr[i]
    #         i += 1
    #         j -= 1

    # return i