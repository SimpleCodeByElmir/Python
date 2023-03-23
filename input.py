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
