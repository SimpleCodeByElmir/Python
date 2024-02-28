# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"


def are_you_playing_banjo(name):
    ret = ""
    chars = ['R', 'r']
    if name[0:1] in chars:
        ret = name + " plays banjo"
    else:
        ret = name + " does not play banjo"
    return ret
    
 
names = ['martin', 'Rikke', 'bravo', 'rolf']
for i in names:
     print(are_you_playing_banjo(i))

