"""
Fibonacci series: 0,1,1,2,3,5,8,13....
"""
def fib_recursive(n):
    """
    Time complexity: 2*(n-1) -> 2powerofn
    """
    if n <= 1:
        return n
    return fib_recursive(n-2) + fib_recursive(n-1)


def fib_dynamic(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2,n+1,1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
        


if __name__ == "__main__":
    print(fib_recursive(5))
    print(fib_dynamic(5))