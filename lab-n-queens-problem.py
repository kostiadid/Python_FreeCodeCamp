def dfs_n_queens(n):

    if n < 1 : 
        return []
    if n < 4:
        return []
    if n ==1:
        return [[0]]
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    

    return matrix



# Queens of the same color don't hit each other, that's the solution, guys... (joke)
