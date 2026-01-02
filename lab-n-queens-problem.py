def dfs_n_queens(n):

    if n < 1 : 
        return []
    if n < 4:
        return []
    if n ==1:
        return [[0]]
    matrix = [[0 for _ in range(n)] for _ in range(n)]    
    pos = [0 for _ in range(n)]
    matrix[0][0] = 1
    prev_row = matrix[0]
    prev_col = matrix[0][0]

    # only one in col 
    if cur_col == prev_col:
        continue
    # only one in diagonal
    if abs(cur_col - prev_col) == abs(cur_row - prev_row):
        continue
        
    return matrix
