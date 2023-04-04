my_arr = [9,8,7,6,5,4,3,2,1,0]

for i in range(9):
  for j in range(9):
    if (my_arr[j] > my_arr[j+1]):
      temp = my_arr[j+1]
      my_arr[j+1] = my_arr[j]
      my_arr[j] = temp

for x in range(len(my_arr)):
  print(my_arr[x], "", end='')

print("\n", end='')
