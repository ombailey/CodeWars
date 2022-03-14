# Write a function maskify that changes all but the last four characters into '#'.
sample = '3424578'
result = '###4578'
def maskify(text):
    masked = ''
    for char in range(len(text[0:-4])):
        masked = masked + '#'
    return masked + text[-4:]

print(maskify(sample) == result)

