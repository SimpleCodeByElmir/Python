# Write a function named first_non_repeating_letter† that takes
# a string input, and returns the first character that is not
# repeated anywhere in the string.

# For example, if given the input 'stress', the function should
# return 't', since the letter t only occurs once in the string,
# and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered
# the same character, but the function should return the correct case
# for the initial letter. For example, the input 'sTreSS'
# should return 'T'.

# If a string contains all repeating characters, it should return
# an empty string ("").


def first_non_repeating_letter(s):
    special_chars = "][@_!#$%^&*()<>?/\|}{~:;,."
    numbers = "0123456789"
    length = len(s)
    ret = ""
    for i in range(0, length):
        counter = 0
        for k in range(0, length):
            if s[i] == s[k] and i == k:
                #print(s[i], s[k])
                continue
            if (s[i] == s[k] or chr(ord(s[i])+32) == s[k] or chr(ord(s[i])-32) == s[k]) and s[k].isalpha() == True:
                counter += 1
            elif (s[i] in special_chars and s[i] == s[k]):
                counter += 1
            elif (s[i] in numbers and s[k] in numbers and s[i] == s[k]):
                print(s[i], s[k])
                counter += 1        
        if counter == 0:
            ret = s[i]
            break
    return ret

#s = "XzFJCz8w3b"
#s = "f4;;jyEdgWDrxTnUi9IMCbuk5D6tXk1;p1NroW:Kp;BDYhr8IhGI BsFMP"
s = "14188T"
print(first_non_repeating_letter(s))

