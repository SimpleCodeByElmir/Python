# copy elements of arr_1 to arr_2. Reversed.

arr_1 = [1,2,3,4]
k = len(arr_1)
arr_2 = [None]*k  # declare arr_2 of size arr_1

i = 0
while k != 0:
    k -= 1
    arr_2[k] = arr_1[i]
    i += 1
    
print(f"{arr_1}\n{arr_2}")

