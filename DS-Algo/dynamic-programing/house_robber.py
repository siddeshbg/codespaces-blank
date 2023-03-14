"""
There are N houses built in a line, each of which contains some value in it. 
A thief is going to steal the maximum value of these houses, but he can’t steal 
in two adjacent houses because the owner of the stolen houses will tell his two 
neighbors left and right sides. The task is to find what is the maximum stolen value.

Ex:
Input: hval[] = {6, 7, 1, 3, 8, 2, 4}
Output: 19
Explanation: The thief will steal 6, 1, 8 and 4 from the house.

Input: hval[] = {5, 3, 4, 11, 2}
Output: 16
Explanation: Thief will steal 5 and 11

Given an array, the solution is to find the maximum sum subsequence where no 
two selected elements are adjacent. So the approach to the problem is a recursive solution. 

So there are two cases:

1. If an element is selected then the next element cannot be selected.
2. if an element is not selected then the next element can be selected.
Use recursion to find the result for both cases.
"""

def max_loot(house_values, index):
    # base case
    if index < 0:
        return 0
    if index == 0:
        return house_values[0]
    
    # if current element is picked, then previous can't be picked
    pick = house_values[index] + max_loot(house_values, index-2)
    # if current element is not picked then previous element is picked
    not_pick = max_loot(house_values, index-1)
    print("max of (%s %s)" % (pick, not_pick))
    return max(pick, not_pick)

# def max_loot_dp(house_values, index):


if __name__ == "__main__":
    house_values = [6, 7, 1, 3]
    print(max_loot(house_values, len(house_values) -  1))

    # hval = [ 6, 7, 1, 3, 8, 2, 4 ]
    # n = len(hval)
    # print("Maximum loot possible : ",max_loot(hval, n - 1));