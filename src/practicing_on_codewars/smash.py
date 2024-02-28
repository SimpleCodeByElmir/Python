# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word.
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!

# Example:
# ['hello', 'world', 'this', 'is', 'great'] 
# =>  'hello world this is great'


def smash(words):
    new_str = ""
    for i in words:
        new_str += i + ' '
    return new_str[0:-1]

words = ['hello', 'everyone']
print(smash(words))


# More "gentle" solution from another User on the codewars.com

#def smash(words):
#    return " ".join(words)
