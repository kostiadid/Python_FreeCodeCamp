# def adjacency_list_to_matrix(graph_list):
#     final_list = []
#     n = len(graph_list)
#     for i in graph_list:
#         current = [[0 for _ in range(n)] for _ in range(n)]
#         for el in  graph_list[i]:
#             current[el] = 1
#     final_list.append(current)
#     return final_list


# def adjacency_list_to_matrix(graph_list):
#     for el, val in graph_list.items():
#         print(f"{el}: {val}")

# adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})

def adjacency_list_to_matrix(list_nums):
    n = len(list_nums)
    matrix = [[0] * n for _ in range(n)]
    for  i, line in  list_nums.items():
        for j  in line:
            #if not j == 0:
               matrix[i][j] = 1   
    for row in matrix:
        print(row)
    return matrix

            
adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})
adjacency_list_to_matrix({0: [1], 1: [0]})
adjacency_list_to_matrix({0: [], 1: [], 2: []})
