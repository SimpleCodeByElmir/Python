# A pangram is a sentence that contains every single letter of
# the alphabet at least once. For example, the sentence
# "The quick brown fox jumps over the lazy dog"
# is a pangram, because it uses the letters A-Z
# at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.


# first way

def is_pangram_1(s):
    res = False
    found_chars = []
    for i in s:
        if (i >= 'A' and i <= 'Z') and (chr(ord(i) + 32) not in found_chars):
            found_chars.append(i)
        elif (i >= 'a' and i <= 'z') and (chr(ord(i) - 32) not in found_chars):
            found_chars.append(i)
    if len(found_chars) >= 26:  # There are 26 unique letters in the English alphabet.
        res = True
    return res


# second way

def is_pangram_2(s):
    res = False
    found_chars = []
    for i in s:
        if i not in found_chars and i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            found_chars.append(i)
    if len(set("".join(found_chars).lower())) >= 26:
        res = True
    return res


string = 'AbCDeFGhIJkLMnOPqRTUVWXyZz'  # True
#string = 'AbCdEfGHIJKLMNOPQrSTuVWXYyyy'  # False

print(is_pangram_1(string))
print(is_pangram_2(string))



# More "gentle" solution from another User on the codewars.com

#import string

#def is_pangram(s):
#    s = s.lower()
#    for char in 'abcdefghijklmnopqrstuvwxyz':
#        if char not in s:
#            return False
#    return True
