# Remove all values from list a that are present in list b
# Take the values in the second list provided and use that to remove the occurences of those values in the first list.

first_list = [1,2,3]
remove_list = [1,2]
result = [3]

def array_diff(list, remove):
    for num in remove:
        num_times = list.count(num)
        for round in range(num_times):
                list.remove(num)
    return list

output = array_diff(first_list, remove_list)
print(output == result)