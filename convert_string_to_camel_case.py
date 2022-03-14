# Take in text that has dash and underscores and convert it into a string without delimeters.
# The first word shouldn't be adjusted.
# The other words need to be converted to title format.
# Return the Camel Cased String

x = 'The-Cat-was_evil'
result = 'TheCatWasEvil'
            
def to_camel_case(text):
    dash_und_index = []
    output = ''
    character = dict(enumerate(text))
    # Getting the index of the delimeters
    for key, val in character.items():
        if val == '_' or val == '-':
           dash_und_index.append(key)

    # Converting the character after the delimeter into title format
    for num in dash_und_index:
        character[num + 1] = character[num + 1].upper()
            
    # Printing out each character besides the delimeters 
    for val in character.values():
        if val == '_' or val == '-':
            continue
        else:
            output = output + val
    return output
    
print(to_camel_case(x))
print(to_camel_case(x) == result)
    
