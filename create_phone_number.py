sample = [1,2,3,4,5,6,7,8,9,0]
result = '(123) 456-7890'

def create_phone_number(numbers):
    output = ''.join([str(num) for num in numbers])
    return f'({output[0:3]}) {output[3:6]}-{output[6:10]}'

print(create_phone_number(sample) == result)