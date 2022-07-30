def read_matrix_from_console():
    n = int(input("Number of rows: "))  # Number of rows
    m = int(input("Number of columns: "))  # Number of columns
    A = []

    print(f"\nThe matrix will be of size {n} x {m}\n")

    for i in range(n):
        row = input(f"Type the {m} elements of the row #{i + 1} separated by a space: ").split()
        for j in range(m):
            row[j] = int(row[j])
        A.append(row)
    return A


def print_matrix_to_console(A):
    print()
    for row in A:
        for element in row:
            print(element, end=" ")
        print()


def run():
    A = read_matrix_from_console()
    print_matrix_to_console(A)


if __name__ == "__main__":
    run()
