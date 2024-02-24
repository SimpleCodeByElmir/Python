import random

def quick_sort(array):
    if len(array) > 1:
        pivot = random.choice(array)
        start = [i for i in array if i < pivot]
        mid = [i for i in array if i == pivot]
        end = [i for i in array if i > pivot]
        array = quick_sort(start) + mid + quick_sort(end)

    return array


array = [9, -8, 7, -6, 5, 4, 3, 2, -1, 0]
array = quick_sort(array)

print(array)


# another one

#def quick_sort(array):
    
#    pivot = random.choice(array)
    
#    start
#    for i in range (0, len(array)):
#        if pivot < array[i]:
#            start[i] = array[i]
#            
#            print(start)
#
#    #sorted_array = start + mid + end
#    #return sorted_array
