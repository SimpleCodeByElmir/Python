

def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array


#array = [8, 5, 6, -1, 2, 3]
array = [9, 8, 7, 6, 5, 4, -4, 3, 2, 2, 1]
bubble_sort(array)
print(array)
