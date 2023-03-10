"""
You’re in charge of selecting a football (soccer) team from a large pool of players. 
Each player has a cost, and a rating. You have a limited budget. 
What is the highest total rating of a team that fits within your budget. 
Assume that there’s no minimum or maximum team size.

General problem statement:
Given n elements, each of which has a weight and a profit, 
determine the maximum profit that can be obtained 
by selecting a subset of the elements weighing no more than w.

Algorithm:
- If weights is empty return 0
- If weights(index) is greater than capacity, ignore it
- Otherwise 2 possibilties
  - We don't select this weight
  - We select this weight, add the profit, reduce this weight from capacity
  - return the max of above 2 
"""

def max_profit_recursive(weights, profits, capacity, index=0):
    if len(weights) == index:
        return 0
    if weights[index] > capacity:
        return max_profit_recursive(weights, profits, capacity, index+1)
    else:
        # Don't select the current weight
        option1 = max_profit_recursive(weights, profits, capacity, index+1)
        # select the current weight
        option2 = profits[index] + max_profit_recursive(weights, profits, capacity-weights[index], index+1)
        return max(option1,option2)


if __name__ == '__main__':
    weights = [5,8,10,12,15]
    profits = [3,7,5,9,7]
    # weights = [5,8,10]
    # profits = [3,7,5]
    capacity = 20
    print(max_profit_recursive(weights,profits,capacity) == 16)
    test0 = {
        'input': {
            'capacity': 165,
            'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
            'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
        },
        'output': 309
    }

    test1 = {
        'input': {
            'capacity': 3,
            'weights': [4, 5, 6],
            'profits': [1, 2, 3]
        },
        'output': 0
    }

    test2 = {
        'input': {
            'capacity': 4,
            'weights': [4, 5, 1],
            'profits': [1, 2, 3]
        },
        'output': 3
    }

    test3 = {
        'input': {
            'capacity': 170,
            'weights': [41, 50, 49, 59, 55, 57, 60],
            'profits': [442, 525, 511, 593, 546, 564, 617]
        },
        'output': 1735
    }

    test4 = {
        'input': {
            'capacity': 15,
            'weights': [4, 5, 6],
            'profits': [1, 2, 3]
        },
        'output': 6
    }

    test5 = {
        'input': {
            'capacity': 15,
            'weights': [4, 5, 1, 3, 2, 5],
            'profits': [2, 3, 1, 5, 4, 7]
        },
        'output': 19
    }

    tests = [test0, test1, test2, test3, test4, test5]