def bubble_sort(arr):
    n = len(arr)
    step = 1
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("Step " + str(step) + ": swap " + str(arr[j]) + " and " + str(arr[j+1]) + ", list become " + str(arr))
                swapped = True
                step += 1
        if not swapped:
            break
    return arr

arr = [int(e) for e in input().split()]
sorted_arr = bubble_sort(arr)