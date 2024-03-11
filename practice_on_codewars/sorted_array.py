# Your task is to make a function that can take
# any non-negative integer as an argument and
# return it with its digits in descending order.
# Essentially, rearrange the digits to create
# the highest possible number.

# Examples:
#    Input: 42145 Output: 54421
#    Input: 145263 Output: 654321
#    Input: 123456789 Output: 987654321


def descending_order(num):
    array = []
    string = ""
    for char in str(num):
        array.append(int(char))
    array.sort(reverse=True)
    for element in array:
        string += str(element)
    return int(string)

print(descending_order(123456789))



# More "gentle" solution from another User on the codewars.com

#def descending_Order(num):
#    return int("".join(sorted(str(num), reverse=True)))

