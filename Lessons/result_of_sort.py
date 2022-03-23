 import os
from bubblesort import bubble_sort
from selectedsort import selection_sort
from envparse import env


env.read_envfile('unsorted_list.env')
UNSORTED_LIST = list(os.environ.get('UNSORTED_LIST'))

print(f'Unsorted list is: {UNSORTED_LIST}')
bubble_sort(UNSORTED_LIST)
print(f'Sorted list by Bubble sort: {UNSORTED_LIST}')

UNSORTED_LIST = list(os.environ.get('UNSORTED_LIST'))

print(f'Unsorted list is: {UNSORTED_LIST}')
selection_sort(UNSORTED_LIST)
print(f'Sorted by Selected sort: {UNSORTED_LIST}')
