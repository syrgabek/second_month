 def selection_sort(UNSORTED_LIST):
    for i in range(len(UNSORTED_LIST)-1):
        min_index = i
        for j in range(i+1, len(UNSORTED_LIST)-1):
            if UNSORTED_LIST[j] < UNSORTED_LIST[min_index]:
                min_index = j
        UNSORTED_LIST[i], UNSORTED_LIST[min_index] = UNSORTED_LIST[min_index], UNSORTED_LIST[i]
