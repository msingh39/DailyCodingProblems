from itertools import combinations


def num_list_additon(numbers, k, total_nums):
    combinations_of_nums = list(combinations(numbers, total_nums))
    sums = map(sum, combinations_of_nums)
    truth_table = []
    idx = []
    for i in range(len(sums)):
        if sums[i] == k:
            truth_table.append(True)
            idx.append(combinations_of_nums[i])
        else:
            truth_table.append(False)
    if any(truth_table):
        return True, idx
    else:
        return False

input = [10,15,3,7]

num_list_additon(input, 17, 2)

