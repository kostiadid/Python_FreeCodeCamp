def square_root_bisection(num, tolerance= 1e-7, max_iter=100):
    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif num == 0 or num == 1:
        print(f'The square root of {num} is {num}')
        return num
    start = 0
    high = max(1,num)
    iterations = 0
    while iterations < max_iter:
        iterations += 1 
        mid = (start + high) / 2
        if high - start <= tolerance:
           print(f"The square root of {num} is approximately {(start + high) / 2}")
           return  (start + high) / 2
        elif  mid * mid > num:
            high = mid
        else :
            start = mid
    print(f'Failed to converge within {iterations} iterations')


