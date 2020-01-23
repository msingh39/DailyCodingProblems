# Daily Coding Problem #4

# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

# My Soltuion

# Function to get positive values from a list
def positive_array(num_list):
    num_list[:] = [i for i in num_list if i >= 0]
    return num_list

#Function to find lowest positive number not in original list
def lowest_positive_number(num_list):
    # Call helper function
    num_list = positive_array(num_list)
    
    # Create a new list from lowest to highest value in original list
    num_list_min_max = list(range(min(num_list),max(num_list) + 2))

    # Loop through and check if value in the new list is in the original, if not return that value
    for i in range(len(num_list_min_max)):
        return [i for i in num_list_min_max if i not in num_list][0]

# Test Case
test_1 = [3,4,-1,1] # Should return 2
print(lowest_positive_number(test_1))

test_2 = [1,2,0] # Should return 3
print(lowest_positive_number(test_2))
