# Write a function that converts lowercase string to uppercase.


def make_upper_case(s):
    new_str = ""
    for i in s:
        if i >= 'a' and i <= 'z':
            new_str += chr(ord(i) - 32)
        else:
            new_str += i
    return new_str 
       
    
string = "everyone hello!"
print(make_upper_case(string))
