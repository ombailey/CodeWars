# Create a function that takes in one argument.
# Should return either True or False (boolean). True if its a prime number, False if its not.
# Number must be greater than 1 if not its false.
# Every number up until the number specified if it divides into another number without a remainder than it is a whole number.
# Must be fast.
sample = 5099
result = True

def is_prime(num):
    prime = 0
    if num <=1:
        return False
    if num <=5099:
        for number in set(range(2,num)):
            if num % number != 0:
                continue
            else:
                prime +=1
        
    else:
        for number in set(range(2,50000)):
            if num % number != 0:
                continue
            else:
                prime +=1 
                
    if prime == 0:
        return True
    else:
        return False
    