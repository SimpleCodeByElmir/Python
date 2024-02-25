string = input()
open_1 = 0
open_2 = 0
open_3 = 0
close_1 = 0
close_2 = 0
close_3 = 0

for i in string:
  if i == '(':
    open_1 += 1
  elif i == '{':
    open_2 += 1
  elif i == '[':
    open_3 += 1
  elif i == ')':
    close_1 += 1
  elif i == '}':
    close_2 += 1
  elif i == ']':
    close_3 += 1

if open_1 != close_1:
  print("Bruh")
elif open_2 != close_2:
  print("Bruh")
elif open_3 != close_3:
  print("Bruh")
else:
  print("Nice")
