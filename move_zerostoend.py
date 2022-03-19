# function must take an array, move all the zeros to the end while preserving the order of the other elements

sample = [1,0,1,2,0,1,3]
result = [1,1,2,1,3,0,0]

def move_zeros(array):
    num_zeros = array.count(0)
    for zero in range(num_zeros):
        array.remove(0)
    array.extend([0] * (num_zeros))
    return array

print(move_zeros(sample) == result)
