arr = [2, 1, 5, 4, 8, 9, 6, 3, 7, 10]
temp = 0
arr_len = len(arr) - 1

for i in range(arr_len):
    for x in range(arr_len - i):
        if (arr[x] > arr[x + 1]):
            temp = arr[x + 1]
            arr[x + 1] = arr[x]
            arr[x] = temp

for i in range(0, (len(arr))):
    print(arr[i])