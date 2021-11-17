def invert(text):

    # First, let's convert the incoming string to an array.
    # This will allow us to more easily use stacks.
    text_array = []
    for letter in text:
        text_array.append(letter)
        
    # Next, create a placeholder string to return the inverted result.
    result_string = ""
    while len(text_array) > 0:
        # Pop off the last item of the array, and add it to our inverted string.
        result_string += text_array.pop()
    return result_string

print(invert("racecar"))
print(invert("ham"))
print(invert("potatoes"))
print(invert("python"))