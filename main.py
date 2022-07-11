import numpy as np
A_height = int(input('Enter the height of the first matrix: '))
print('Enter the first matrix'.format(A_height))
A_input = [list(map(float, input().split())) for _ in range(A_height)]

B_height = int(input('\nEnter the height of the second matrix: '))
print('Enter the second matrix'.format(B_height))
B_input = [list(map(float, input().split())) for _ in range(B_height)]

'''A_txt = open('mat_1.txt', 'r')
B_txt = open('mat_2.txt', 'r')'''
matrix_A = np.array(A_input)
matrix_B = np.array(B_input)


def matrix_splitting(A, B):
    A_width = len(A[0])
    A_height = len(A)

    B_width = len(B[0])

    line_sep_index = int(A_width // 2)
    column_sep_index = int(A_height // 2)

    bline_sep_index = int(B_width // 2)

    A_11 = A[0:column_sep_index, 0:line_sep_index].tolist()
    A_12 = A[0:column_sep_index, line_sep_index::].tolist()
    A_21 = A[column_sep_index::, 0:line_sep_index].tolist()
    A_22 = A[column_sep_index::, line_sep_index::].tolist()

    B_11 = B[0:line_sep_index, 0:bline_sep_index].tolist()
    B_12 = B[0:line_sep_index, bline_sep_index::].tolist()
    B_21 = B[line_sep_index::, 0:bline_sep_index].tolist()
    B_22 = B[line_sep_index::, bline_sep_index::].tolist()

    return [A_11, A_12, A_21, A_22], [B_11, B_12, B_21, B_22]


A, B = matrix_splitting(matrix_A, matrix_B)


def multiplication(A, B, a_height, b_width, n=2):

    if n == 2:
        C_11 = (multiplication(A[0], B[0], len(A[0]), len(B[0][0]), n=1) + multiplication(A[1], B[2], len(A[1]), len(B[2][0]), n=1)).tolist()
        C_12 = (multiplication(A[0], B[1], len(A[0]), len(B[1][0]), n=1) + multiplication(A[1], B[3], len(A[1]), len(B[3][0]), n=1)).tolist()
        C_21 = (multiplication(A[2], B[0], len(A[2]), len(B[0][0]), n=1) + multiplication(A[3], B[2], len(A[3]), len(B[2][0]), n=1)).tolist()
        C_22 = (multiplication(A[2], B[1], len(A[2]), len(B[1][0]), n=1) + multiplication(A[3], B[3], len(A[3]), len(B[3][0]), n=1)).tolist()
        return [C_11, C_12, C_21, C_22]
    if n == 1:
        C = [[0 for row in range(b_width)] for col in range(a_height)]
        for i in range(a_height):
            for j in range(b_width):
                sum = 0
                for k in range(len(A[0])):
                    sum += A[i][k] * B[k][j]
                C[i][j] = sum
        return np.array(C)


C = multiplication(A, B, len(A), len(B[0]), n=2)

print()
for i in range(len(C[0])):
    print(*C[0][i], *C[1][i])

for i in range(len(C[2])):
    print(*C[2][i], *C[3][i])
