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
    special_chars = ":,.!?"
    for word in string.split():
        if len(word) >= 5:
            word = word[::-1]
            for i in range(0, len(word)):
                if word[i] in special_chars:
                    word = word.replace(word[i], '') + word[i]  # moving ":,.!?" in the end.
                    break
        new_str += word + " "
    return new_str.strip()

string = "Stop Snipping My Words!"
print(spin_words(string))  # Stop gninnipS My sdroW!


# More "gentle" solution from another User on the codewars.com

#1
#def spin_words(sentence):
#    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

#2
#def spin_words(sentence):
#    words = [word for word in sentence.split(" ")]
#    words = [word if len(word) < 5 else word[::-1] for word in words]
#    return " ".join(words)

#3
#def spin_words(sentence):
#    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())

