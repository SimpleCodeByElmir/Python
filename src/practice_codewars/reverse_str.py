# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'


def reverse_str(string):
    new_string = ""
    n = len(string) - 1
    while n > -1:
        new_string += string[n]
        n -= 1
    return new_string

string = "world"    
print(reverse_str(string))



# More "gentle" solution from another User on the codewars.com

#def solution(str):
#  return str[::-1]

