def fibonacci(n):
    sequence = [0, 1]
    if n < 0 or not isinstance(n, int):
        return "Error"
    prev1 = 0
    prev2 = 1
    if n == 0:
        return prev1
    if n == 1:
        return prev2
    for i in range(n - 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return prev2

