# From the two strings (which are only letters from a to z) return a list that contains only the distinct letters between the two and is sorted.
# 1) function that takes two arguments
# 2) Checks to see what letters are distinct in each string
# 3) Combine the distrinct letters and sort them
# 4) Print the result as a string. 

a = "aretheyhere"
b = "yestheyarehere"
result = "aehrsty"

def longest(a1, a2):
    combined = set()
    for char in a1:
        combined.add(char)
    for char in a2:
        combined.add(char)
        return ''.join(sorted(combined))
    
print(longest(a,b) == result)

# Found out set can take two functions so heres more efficient code

# def longest(a1,a2):
# return ''.join(sorted((set(a1 + a2)))
