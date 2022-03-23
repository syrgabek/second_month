def bubble_sort(UNSORTED_LIST):
    for n in range(len(UNSORTED_LIST)-1, 0, -1):
        for i in range(n):
            if UNSORTED_LIST[i] > UNSORTED_LIST[i + 1]:
                UNSORTED_LIST[i], UNSORTED_LIST[i + 1] = UNSORTED_LIST[i + 1], UNSORTED_LIST[i]








