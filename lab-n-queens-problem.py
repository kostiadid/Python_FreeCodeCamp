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

    curr = 0
    prev_row = 0
    def move(curr):
        if curr == n:
            return
        for j in range(n):
                confl  = False
                prev_col = matrix[prev_row].index(1)
                if  j == prev_col:
                    confl = True
                    break
                if abs(j - prev_col) == abs(i - prev_row):
                    confl = True
                    break
                if confl:
                    continue
            
                matrix[curr][j] = 1
                move(curr+1)
                matrix[curr][j] = 0
        
         

    move(curr+1)
    print(matrix)
    return matrix

dfs_n_queens(5)  
