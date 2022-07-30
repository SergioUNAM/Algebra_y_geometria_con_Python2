"""The following functions presented perform standard operations on matrices: addition, multiplication by a number and transposition."""

"""Las siguientes funciones presentadas realizan operaciones estándares con matrices: suma, multiplicación por un escalar y transposición"""


def matrix_add(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = [[0 for j in range(len(A[0]))] for i in range(
            len(A))]  # Create a null matrix C, with the same dimension as matrices A and B | Crea un matriz nula C, con la misma dimensión que las matrices A y B

        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] + B[i][j]

        return C


def matrix_mult_by_scalar(A, alpha):
    C = [[0 for j in range(len(A[0]))] for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = alpha * A[i][j]
    return C


def matrix_substract(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = [[0 for j in range(len(A[0]))] for i in range(len(A[0]))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] - B[i][j]

        return C


def matrix_transpose(A):
    C = [[0 for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[j][i] = A[i][j]

    return C


def print_matrix(X):
    for row in X:
        for element in row:
            print(element, end=" ")
        print()
    print()


def run():
    A = [[1, 1], [2, 2]]
    B = [[2, 2], [3, 3]]

    print("Matrix A: ")
    print_matrix(A)
    print("Matrix B: ")
    print_matrix(B)

    print("Sum of matrices: ")
    S = matrix_add(A, B)
    print_matrix(S)

    alpha = 3
    print(f"Multiplication by a scalar alpha = {alpha}: ")
    M = matrix_mult_by_scalar(A, 3)
    print_matrix(M)

    print("Rest of matrices: ")
    R = matrix_substract(A, B)
    print_matrix(R)

    print("Matrix transpose: ")
    T = matrix_transpose(A)
    print_matrix(T)

if __name__ == "__main__":
    run()
