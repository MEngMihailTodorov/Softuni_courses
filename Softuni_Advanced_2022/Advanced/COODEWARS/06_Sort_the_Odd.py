def sort_array(arr):
    length = len(arr)
    for i in range(length):
        if arr[i] % 2 == 1:
            for j in range(0,  i):
                if arr[j] % 2 == 1:
                    if arr[j] > arr[i]:
                        smaller = arr[i]
                        larger = arr[j]
                        arr[j] = smaller
                        arr[i] = larger
                    else:
                        pass
                else:
                    pass

    return arr


source_array = list(map(int, input().split()))
print(sort_array(source_array))