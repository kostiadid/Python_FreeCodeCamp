def square_root_bisection(num, tolerance=0.01, max_iter=100):
    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif num == 0 or num == 1:
        print(f'The square root of {num} is {num}')
        return num
