def selection_sort(arr):
    n = len(arr)
    step = 1
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print("Step " + str(step) + ": swap " + str(arr[i]) + " and " + str(arr[min_idx]) + ", list become " + str(arr))
            step += 1
    return arr

arr = [int(e) for e in input().split()]
sorted_arr = selection_sort(arr)