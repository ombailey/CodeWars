# In each string a word will have a number in it and thats the order it should be in for the result.
# If string is empty, return an empty string. Numbers will be from 1-9
# 1) Create a function that takes string as input. Split words. Find number within each word and match it to the word. Put string together in order.
sample = ""
result = ""

def order(sentence):
    output = []
    if sentence == '':
        return ''
    words = sentence.split()
    for num in range(1,10):
        for word in words:
            if word.find(f'{num}') > -1:
                output.append(word)
    
    return ' '.join(output)
print(order(sample) == result)
    