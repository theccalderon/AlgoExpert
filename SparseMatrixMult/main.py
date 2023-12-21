# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a) == 0 or len(matrix_b) == 0:
        return [[]]
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    w, h = len(matrix_b[0]), len(matrix_a)
    matrix_c = [[0 for x in range(w)] for y in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(len(matrix_b)):
                matrix_c[i][j] += matrix_a[i][k]*matrix_b[k][j]
    return matrix_c

def sparse_matrix_multiplication1(matrix_a, matrix_b):
    if len(matrix_a) == 0 or len(matrix_b) == 0:
        return [[]]
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    w, h = len(matrix_b[0]), len(matrix_a)
    matrix_c = [[0 for x in range(w)] for y in range(h)]
    for i in range(h):
        for k in range(len(matrix_b)):
            if matrix_a[i][k] == 0:
                continue
            for j in range(w):
                matrix_c[i][j] += matrix_a[i][k]*matrix_b[k][j]
    return matrix_c


def get_dict_of_nonzero_cells(matrix):
    dict_of_nonzero_cells = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                dict_of_nonzero_cells[(i,j)] = matrix[i][j]
    return dict_of_nonzero_cells


def sparse_matrix_multiplication_final(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]

    sparse_a = get_dict_of_nonzero_cells(matrix_a)
    sparse_b = get_dict_of_nonzero_cells(matrix_b)

    matrix_c = [[0 for x in range(len(matrix_b[0]))] for y in range(len(matrix_a))]
    for i,k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k,j) in sparse_b.keys():
                matrix_c[i][j] += sparse_a[(i,k)] * sparse_b[(k,j)]
    return matrix_c

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix_a = [
        [46, 0, 0],
        [45, 47, 0],
        [0, 0, 0],
        [34, 0, 25],
        [0, 2, 0],
        [0, 0, 0]
    ]
    matrix_b = [
        [26, 34, 20, 31, 34, 15],
        [38, 30, 23, 1, 45, 22],
        [47, 9, 9, 5, 9, 31]
    ]
    print(sparse_matrix_multiplication_final(matrix_a,matrix_b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
