def square_root_bisection(number,error,iterations=1000):

    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0 or  number == 1 :
        return f"The square root of {number} is {number}"
    root = number ** 0.5
    return f"The square root of {square_target} is approximately {root}"
