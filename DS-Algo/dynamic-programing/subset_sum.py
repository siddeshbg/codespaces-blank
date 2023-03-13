"""
Given a set of non-negative integers, and a value sum, 
determine if there is a subset of the given set with sum equal to given sum. 

Example:
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.

Recursive Approach:
1. Consider the last element and now the required sum = target sum - 'last' element 
    and number of elements = total elements - 1
2. Leave the 'last' element and now the required sum = target sum 
and number of elements = total elements - 1
"""

def is_subset_sum(input_set, n, target_sum):
    # Base cases
    if (target_sum == 0):
        return True
    if (n == 0):
        return False
    
    # If the last element is greater than sum, then ignore it
    if input_set[n-1] > target_sum:
        return is_subset_sum(input_set, n - 1, target_sum)
    
    # check if sum can be obtained by any of the following
    # a. including last element
    # b. excluding last element
    return is_subset_sum(input_set, n - 1, target_sum - input_set[n-1]) or is_subset_sum(input_set, n - 1, target_sum)
    

if __name__ == '__main__':
    input_set = [3, 34, 4, 12, 5, 2]
    target_sum = 9
    print(is_subset_sum(input_set, len(input_set), target_sum))

    print(is_subset_sum([7, 17, 8, 2, 1, 5], 6, 41))
