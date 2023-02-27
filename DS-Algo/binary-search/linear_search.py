"""
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards
as possible. 
Write a function to help Bob locate the card.

Source: https://jovian.com/learn/data-structures-and-algorithms-in-python/lesson/lesson-1-binary-search-linked-lists-and-complexity

Complexity: 
Time: O(n)
Space: O(1)
"""

def linear_search(cards, query):
    """
    Cards: List of numbers
    Query: A number to search
    """
    position = 0
    while position < len(cards):
        if query == cards[position]:
            return position
        position += 1
    return -1

if __name__ == "__main__":
    test = {
        "input": {
            "cards": [79, 70, 62, 54, 44, 37, 21, 19, 7, 3, 1],
            "query": 21
        },
        "output": 6
    }
    print(linear_search(test["input"]["cards"], test["input"]["query"]) == test["output"])

    test2 = {
        "input": {
            "cards": [79, 70, 62, 54, 44, 37, 21, 19, 7, 3, 1],
            "query": 66
        },
        "output": -1
    }
    print(linear_search(test2["input"]["cards"], test2["input"]["query"]) == test2["output"])

    test3 = {
        "input": {
            "cards": [],
            "query": 66
        },
        "output": -1
    }
    print(linear_search(test3["input"]["cards"], test3["input"]["query"]) == test3["output"])