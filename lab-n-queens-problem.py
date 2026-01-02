def dfs_n_queens(n):

    if n < 1 : 
        return []
    if n < 4:
        return []
    if n ==1:
        return [[0]]
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    pos = [0 for _ in range(n)]

    # for q in range (n):
    matrix[0][0] = 1
    prev_row = matrix[0]
    prev_col = matrix[0][0]

    for q in range (n,2):
        cur_row = [q]
        cur_col = [q] 
        if cur_col == prev_col:
            continue
    return matrix



# prev_row 
# current_row
#  prev_col
#  prev_row
#if abs(candidate_row - prev_row) == abs(candidate_col - prev_col):
#     safe = True
# for prev_row in range(current_row):
#     prev_col = solution[prev_row]
    
#     # вертикаль
#     if candidate_col == prev_col:
#         safe = False
#         break

#     # диагонали
#     if abs(candidate_col - prev_col) == abs(current_row - prev_row):
#         safe = False
#         break
