""" #Bubble sort algorithm

nums = [9,8,7,6,5,4,3,2,1,0]
nums_amount = len(nums)
temp = 0

print(f"starting to sort numbers:\n{nums}")

for i in range(nums_amount-1):
    for c in range(nums_amount-1):
      if nums[c] > nums[c+1]:
        temp = nums[c]
        nums[c] = nums[c+1]
        nums[c+1] = temp
print(f"sorted:\n{nums}")
"""

# Bubble sort function
def bubble_sort(numbers_to_sort):
  nums = numbers_to_sort.copy()
  nums_amount = len(nums)
  temp = 0

  print(f"*******\nstarting to sort numbers:\n{nums}")
  for i in range(nums_amount-1):
    for c in range(nums_amount-1):
      if nums[c] > nums[c+1]:
        temp = nums[c]
        nums[c] = nums[c+1]
        nums[c+1] = temp
  print(f"*******\nsorted:\n{nums}")
  print(f"#######\nthe original array:\n{numbers_to_sort}")


bubble_sort([100,-1,31,2,3,4,5])
