# Set Find Pairs ( Interview Question)

# Instructions
# You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

# Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each array does not contain duplicate values.

# The tests for this exercise assume that arr1 is the list being converted to a set.

# Input

# Your function should take in the following inputs:

# arr1: a list of integers

# arr2: a list of integers

# target: an integer


# Output

# Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.



# Example 1:

# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]
# target = 9

# pairs = find_pairs(arr1, arr2, target)
# print (pairs)
# # Expected output: [(3, 6)]
# # Explanation: There's only one pair that adds up to 9: 3 from arr1 and 6 from arr2.


# Example 2:

# arr1 = [0, 1, 2]
# arr2 = [7, 8, 9]
# target = 10

# pairs = find_pairs(arr1, arr2, target)
# print (pairs)
# # Expected output: [(1, 9), (2, 8)]
# # Explanation: The pairs that add up to 10 are (1, 9) and (2, 8).


# Example 3:

# arr1 = [1, 2, 3, 5]
# arr2 = [1, 3, 4, 5]
# target = 6

# pairs = find_pairs(arr1, arr2, target)
# print(pairs)
# # Expected output: [(5, 1), (3, 3), (2, 4), (1, 5)]
# # Explanation: The pairs that add up to 6 are (5, 1), (3, 3), 
# # (2, 4), and (1, 5). Each pair consists of one element from arr1 
# # and one element from arr2 that together sum to the target value.


# Example 4:

# arr1 = [1, 2, 3, 5]
# arr2 = [1, 3, 4, 5]
# target = 11

# pairs = find_pairs(arr1, arr2, target)
# print(pairs)
# # Expected output: []
# # Explanation: There are no pairs in arr1 and arr2 that add up to 11.


def find_pairs(arr1, arr2, target):
    output = []
    arr1_set = set(arr1)
    for num in arr2:
        if target - num in arr1_set:
            output.append((target - num, num))
            
    return output

# arr1 = [0, 1, 2]
# arr2 = [7, 8, 9]
# target = 10

# pairs = find_pairs(arr1, arr2, target)
# print (pairs)