name = input ("\nYour name: ")

len = 0
for i in name:
  if i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z':
    len += 1
  else:
    len = -1
    break

if len > 0:
  print("Hello", name)
  print(f"Your name contains {len} symbols.")
else:
  print("Only letters, please.")

if len > 0:
  flag = input ("Choose \"name-modification\" mod, input 1, 2 or 3: ")
  print("\n", end='')
  for i in name:
    if flag == '1':
      if i >= 'A' and i <= 'G' or i >= 'a' and i <= 'g':
        print(f"{i}@", end='')
      else:
        print(f"{i}%$*", end='')
    elif flag == '2':
      if i >= 'H' and i <= 'P' or i >= 'h' and i <= 'p':
        print(f"{i}#", end='')
      else:
        print(f"{i}!#%", end='')
    elif flag == '3':
      if i >= 'Q' and i <= 'Z' or i >= 'q' and i <= 'z':
        print(f"{i}%", end='')
      else:
        print(f"{i}?%@", end='')
    else:
      print("Incorrect. Only 1,2 or 3.")
      break

  if flag >= '1' and flag <= '3':
    print("\n")
    more = input ("Want some more?\nY/N: ")
    if more == "Y":
      while len > -1:
        print(f"{name} ha-ha-ha\nbe-be-be")
        len += 1
        if len > 300000:
          print("Okey... press Ctrl+C to stop Me)))")
    else:
      print("It's sad... See you (")
