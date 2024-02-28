# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.
# Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and
# it's not part of it, see the sample tests.

# For example (Input -> Output):
# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)


def summation(num):
    res = 0
    if num == 1:
        res = 1
    else:
        for i in range (1, num+1):
            res += i
    return res
    
print(summation(0))
print(summatrion(8))


# More "gentle" solution from another User on the codewars.com

#def summation(num):
#    return sum(range(1,num+1))
