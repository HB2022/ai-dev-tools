def input_matrix(name):
    """Prompt the user to enter a matrix's dimensions and elements."""
    print(f"\n--- Matrix {name} ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    print(f"Enter elements row by row ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = float(input(f"Element [{i+1}][{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def print_matrix(matrix, label="Matrix"):
    """Print a matrix with a label."""
    print(f"\n{label}:")
    for row in matrix:
        print("  ".join(f"{elem:8.2f}" for elem in row))

def add_matrices(A, B):
    """Return the sum of two matrices (same dimensions)."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def subtract_matrices(A, B):
    """Return A - B (same dimensions)."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

def multiply_matrices(A, B):
    """Return A * B (columns of A must equal rows of B)."""
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in first matrix must equal number of rows in second.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_val = 0
            for k in range(len(B)):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val)
        result.append(row)
    return result

def scale_matrix(matrix, factor):
    """Multiply every element of the matrix by a scalar factor."""
    result = []
    for row in matrix:
        new_row = [elem * factor for elem in row]
        result.append(new_row)
    return result

def transpose_matrix(matrix):
    """Return the transpose of the matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def determinant(matrix):
    """Compute determinant of a square matrix (recursive)."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det

def inverse_matrix(matrix):
    """Return the inverse of a square matrix using Gauss-Jordan elimination."""
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Matrix must be square to compute inverse.")
    # Create augmented matrix [A | I]
    aug = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]
    # Perform elimination
    for col in range(n):
        # Find pivot
        pivot = aug[col][col]
        if pivot == 0:
            # Swap with a lower row
            for r in range(col+1, n):
                if aug[r][col] != 0:
                    aug[col], aug[r] = aug[r], aug[col]
                    pivot = aug[col][col]
                    break
            else:
                raise ValueError("Matrix is singular, inverse does not exist.")
        # Normalize pivot row
        for j in range(2*n):
            aug[col][j] /= pivot
        # Eliminate other rows
        for r in range(n):
            if r != col:
                factor = aug[r][col]
                for j in range(2*n):
                    aug[r][j] -= factor * aug[col][j]
    # Extract inverse
    inv = [row[n:] for row in aug]
    return inv

def main():
    print("Matrix Operations Program")
    print("=" * 30)
    
    A = input_matrix("A")
    B = input_matrix("B")
    
    while True:
        print("\n" + "=" * 30)
        print("Choose an operation:")
        print("1. Add (A + B)")
        print("2. Subtract (A - B)")
        print("3. Multiply (A * B)")
        print("4. Scale one matrix by a factor")
        print("5. Inverse of each matrix")
        print("6. Transpose of each matrix")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "7":
            print("Exiting program. Goodbye!")
            break
        
        try:
            if choice == "1":
                result = add_matrices(A, B)
                print_matrix(result, "A + B")
            elif choice == "2":
                result = subtract_matrices(A, B)
                print_matrix(result, "A - B")
            elif choice == "3":
                result = multiply_matrices(A, B)
                print_matrix(result, "A * B")
            elif choice == "4":
                which = input("Scale which matrix? (A/B): ").strip().upper()
                factor = float(input("Enter scale factor: "))
                if which == "A":
                    result = scale_matrix(A, factor)
                    print_matrix(result, f"Scaled A (factor {factor})")
                elif which == "B":
                    result = scale_matrix(B, factor)
                    print_matrix(result, f"Scaled B (factor {factor})")
                else:
                    print("Invalid matrix choice.")
            elif choice == "5":
                print("\nInverse of A:")
                try:
                    invA = inverse_matrix(A)
                    print_matrix(invA, "A⁻¹")
                except ValueError as e:
                    print(e)
                print("\nInverse of B:")
                try:
                    invB = inverse_matrix(B)
                    print_matrix(invB, "B⁻¹")
                except ValueError as e:
                    print(e)
            elif choice == "6":
                print("\nTranspose of A:")
                print_matrix(transpose_matrix(A), "Aᵀ")
                print("\nTranspose of B:")
                print_matrix(transpose_matrix(B), "Bᵀ")
            else:
                print("Invalid operation choice. Please enter a number from 1 to 7.")
        except ValueError as e:
            print("Error:", e)
        
        # Ask if user wants to continue (optional but good)
        cont = input("\nPress Enter to continue to the menu, or type 'q' to quit: ").strip().lower()
        if cont == 'q':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()