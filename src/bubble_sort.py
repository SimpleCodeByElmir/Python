my_arr = [9,8,7,6,5,4,3,2,1,0]

for i in range(10):
  for j in range(9):
    if (my_arr[j] > my_arr[j+1]):
      temp = my_arr[j+1]
      my_arr[j+1] = my_arr[j]
      my_arr[j] = temp
      print(f"{i} ", end='')
      break

print("\n", end='')
