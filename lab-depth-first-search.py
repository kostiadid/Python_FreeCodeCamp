def dfs(matrix,n):
    visited = [False] * len(matrix)
    result = []
    def dfs_visit(i):
        visited[i] = True
        result.append(i)
        for j in range(len(matrix)-1,-1,-1):        #for j in range(len(matrix)):      here  was my main issue   --> 
            if matrix[i][j] == 1 and not visited[j]:
                dfs_visit(j)
    dfs_visit(n)
    print(result)
    return result
dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)
