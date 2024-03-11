# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]


def digitize(n):
    res = []
    string = str(n)
    x = len(string) - 1
    while x != -1:
        res.append(int(string[x]))
        x -= 1
    return res
    

print(digitize(35231))


# More "gentle" solutions from other Users on the codewars.com

#def digitize(n):
#    return [int(x) for x in str(n)[::-1]]

#def digitize(n):
#    return map(int, str(n)[::-1])
