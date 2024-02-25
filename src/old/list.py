import time

# This algorithm prints each day of each month in the 2023. (Working with "lists" type).
# For example, this script can be used to make some operations needed to be done each day. 

year = 2023;
months = [
["january", 31],
["february", 28],
["march", 31],
["april", 30],
["may", 31],
["june", 30],
["july", 31],
["august", 31],
["september", 30],
["october", 31],
["november", 30],
["december", 31],
]

print("#year:", year, "\n")
#print(months[0][1])
#print(months[0][1]+months[1][1])

while (1):
  for i in range(12):
    print("#month =", months[i][0])
    print("*days in month =", months[i][1])
    for k in range(months[i][1]):
      print("day", k+1)
  time.sleep (3)
  year += 1
  break

print("year itterated and now is:", year)
