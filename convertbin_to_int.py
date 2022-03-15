# Given an array of ones and zeros, convert the equivalent binary value to an integer
# 1) Convert list elements into a single string.
# 2) Convert string into integer

def binary_array_to_number(array):
    return int("".join(map(str, array)), 2)

sample = [1,0,1,1]
result = 11
print(binary_array_to_number(sample) == result)