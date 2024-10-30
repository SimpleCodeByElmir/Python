def binary_search(array, value):
    low = 0
    high = len(array) - 1
    result = 0

    counter = 0
    while low <= high:
        mid = (low+high) // 2
        guess = array[mid]
        if guess == value:
            result = mid
            break
        elif guess > value:
            high = mid - 1
        else:
            low = mid + 1
        counter = counter + 1
    print(f"Number found in {counter} iterations.")
    return result

array = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(binary_search(array,8))
