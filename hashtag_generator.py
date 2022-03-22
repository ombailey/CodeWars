sample = "    Hello     World   " 
result = '#HelloWorld'

def generate_hashtag(sentence):
    if sentence == '':
        return False
    words = sentence.split()
    output =[]
    for word in words:
        output.append(word.title())
    if len('#' + ''.join(output).strip()) > 140:
        return False
    else:
        return '#' + ''.join(output).strip()

print(generate_hashtag(sample) == result)