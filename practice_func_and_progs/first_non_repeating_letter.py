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
    #copy = s
    length = len(s)
    ret = ""
    for i in range(0, length-1):
        print(s[0:i+1])
        print(s[i+1::-1][0])
        break
        #test_str = s[0:i] + s[i:-1]
        #print(test_str)
        #if not s[i] in test_str:
         #   print(test_str)
          #  ret = s[i]
           # break
    return ret
        #for k in range(0, length-1):
        #    if not s[k] in s:
        #        if k == i:
        #            continue
        #        else:
        #            ret = s[k]
        #            return ret
    #return ret

s = "stress"
print(first_non_repeating_letter(s))
#if not s[2] in s:
#    print("not")
#else:
#    print("yes")
