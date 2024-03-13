# Write a function that takes in a string of one or more words,
# and returns the same string, but with all words that have five
# or more letters reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

# Examples:
#    "Hey fellow warriors"  --> "Hey wollef sroirraw" 
#    "This is a test        --> "This is a test" 
#    "This is another test" --> "This is rehtona test"


# my simple solution with extraneous function split() 

def spin_words(string):
    new_str = ""
    for word in string.split():
        if len(word) >= 5:
            word = word[::-1]
        new_str += word + " "
    return new_str

string = "Stop Snipping My Words!"
print(spin_words(string))


