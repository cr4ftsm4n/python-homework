def saddle_points(matrix):
    pivot = list(zip(* matrix))
    r = len(matrix)
    if r == 0:
        return set()
    c = len(matrix[0])
    for i in range(0, r):
        if len(matrix[i]) != c:
            raise ValueError("bad matrix")
    result = []
    for i in range(0, r):
        for j in range(0, c):
            this_row = matrix[i]
            this_col = pivot[j]
            point = matrix[i][j]
            if point >= max(this_row) and point <= min(this_col):
                result.append((i, j))
    return set(result)
