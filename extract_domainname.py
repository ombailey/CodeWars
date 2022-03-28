sample = 'https://www.google.com'
result = 'google'

def domain_name(url):
    if 'www' in url:
        beg = str(url).find('.') + 1
    elif 'http://' in url or 'https://' in url:
        beg = str(url).find('/') + 2
    else:
        beg = 0 
    output =[]
    for char in url[beg:]:
        if char != '.':
            output.append(char)
        else:
            break
    return ''.join(output)

print(domain_name(sample))