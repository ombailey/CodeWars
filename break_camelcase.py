x = 'camelCase'
result = 'camel Case'
def break_camelcase(string):
    output = []
    for char in string:
        if char == str(char).upper():
            output.append(' ' + char)
        else:
            output.append(char)
    return ''.join(output)

print(break_camelcase(x) == result)
