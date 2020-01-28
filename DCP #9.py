# Daily Coding Problem #9

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# My Solution

def get_larget_sum (num_list):
    # Get the max value from list and the idx for that value
    temp_list = num_list
    max_1 = max(num_list)
    max_1_idx = num_list.index(max_1)
 
    # Remove that value from the list
    temp_list.pop(max_1_idx)

    max_2 = max(temp_list)
    max_2_idx = num_list.index(max_2)

    # Check if the value is adjacent to the previous max
    idx_prev = max_1_idx - 1
    idx_next = max_1_idx + 1
    if(max_2_idx == idx_prev or max_2_idx == idx_next):
        temp_list.pop(max_2_idx)
        max_2 = max(temp_list)

    # Sum up the value and return the solution 
    sum = max_1 + max_2
    return sum


# Test Cases
num_list = [2,4,6,8] 
print(get_larget_sum(num_list)) # Should return 12

num_list = [5,1,1,5]
print(get_larget_sum(num_list)) # Should return 10