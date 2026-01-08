# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", 'o')  =>  1
# ("Hello", 'l')  =>  2
# ("", 'z')       =>  0
# Notes
# The first argument can be an empty string

def str_count(string, letter):
    if not isinstance(string, str) or not isinstance(letter, str):
        return "Please input strings"

    if len(letter) > 1: 
        return "letter can't be more than one character"

    counter = 0

    print("Check execution")

    #Edge cases:
    string = string.lower()
    letter = letter.lower()

    #Loop -> looking at each character in the string individually
    for char in string: 
        #Compare the letter to the char for each iteration
        if char == letter: 
            counter+=1
            
    return counter


# Happy Path:
# "apples" - "a" -> 1
# "apples" - "b" -> 0
# "" - "c" -> 0
# "apples" - "" -> 0

# Edge cases: 
# What about casing? "APPLES" - "a" -> "1" 
# What about casing? "apples" - "A" -> "1"

# Error handling:
# Do some error handling -> refuse things that aren't a string -> return "Please input strings"
# "apples" -> "aa" - "Only one letter for second argument" 

print("Edge case: \n", str_count("APPLES", "a"))
print("Edge case \n", str_count("apples", "A"))
print("letter and string are wrong type: \n", str_count(1, 3))
print("letter is wrong type: \n", str_count("apples", 3))
print("happy path:\n", str_count("apples", "p"))
print("multiple characters letter:\n", str_count("apples", "beaa"))
print("empty string:\n", str_count("apples", " "))