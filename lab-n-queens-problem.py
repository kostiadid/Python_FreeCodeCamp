def dfs_n_queens(n):
    if n < 1:
        return []
    if n == 1:
        return [[0]]
    if n < 4: 
        return []

    result = []              
    solution = [-1] * n     

    def move(curr):
        if curr == n:      
            result.append(solution.copy())
            return
        for j in range(n):   
            conflict = False
            for prev_row in range(curr):
                prev_col = solution[prev_row]
                #cannot stand on a vertical or diagonal line (we change the horizontal line with each iteration anyway)
                if j == prev_col or abs(j - prev_col) == abs(curr - prev_row):
                    conflict = True
                    break
            if conflict:
                continue
            solution[curr] = j  
            move(curr + 1)    
            solution[curr] = -1 

    move(0)
    return result

solutions = dfs_n_queens(5)
for sol in solutions:
    print(sol)
