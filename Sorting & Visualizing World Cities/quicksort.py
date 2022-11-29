# Author: Chip Nguyen
# Date: 11/06/2022
# Purpose: Lab 3 - Quick Sort Algorithm

# Function to partition the given list
def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p
    pivot = the_list[r]

    while j < r:
        if compare_func(the_list[j], pivot):
            i = i + 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
            j = j + 1

        else:
            j = j + 1

    the_list[i + 1], the_list[r] = pivot, the_list[i + 1]

    return i + 1

def quicksort(the_list, p, r, compare_func):
    if p >= r:
        return None

    q = partition(the_list, p, r, compare_func)
    quicksort(the_list, p, q - 1, compare_func)
    quicksort(the_list, q + 1, r, compare_func)

def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)