# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

# Examples (input -> output):
#   6, "I"     -> "IIIIII"
#   5, "Hello" -> "HelloHelloHelloHelloHello"


def repeat_str(repeat, string):
    new_str = ""
    for i in range(0, repeat):
        new_str += string
    return new_str
    
    
string = "Hi"
print(repeat_str(5, string))


# More "gentle" solution from another User on the codewars.com

#def repeat_str(repeat, string):
#    return string*repeat
