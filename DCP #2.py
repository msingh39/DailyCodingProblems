#Daily Coding Problem Problem #2

#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#My solution
import numpy as np
from functools import reduce

def array_mult(array):
    solution = []
    for i in range(len(array)):
        solution.append(reduce(lambda x,y: x*y, (array[:i] + array[i+1:])))
    return solution


#Test Solution
input = [1,2,3,4,5] #Expected output is [120,60,40,30,24]
print(array_mult(input))

input = [3,2,1] #Expected output is [2,3,6]
print(array_mult(input))
