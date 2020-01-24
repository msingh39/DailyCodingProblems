# Daily Coding Problem #5

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    return lambda f : f(a, b)

# Implement car and cdr

def car(pair):
    first_num = lambda a,b : a
    return pair(first_num)

def cdr(pair):
    second_num = lambda a,b: b
    return pair(second_num)

# Test Solution 
print(car(cons(3,4))) # Should return 3
print(cdr(cons(3,4))) # Should return 4