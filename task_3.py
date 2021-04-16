import utils

@utils.time_for_function
def function(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                result.append((i, j))
    return result