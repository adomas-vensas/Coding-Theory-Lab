
def multiply_matrices(A:list, B:list) -> list[list]:
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B.")
    
    # Resultant matrix dimensions: rows of A x columns of B
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Manual matrix multiplication
    for i in range(len(A)):  # Rows of A
        for j in range(len(B[0])):  # Columns of B
            for k in range(len(B)):  # Rows of B or Columns of A
                result[i][j] += A[i][k] * B[k][j]
    
    return result


def multiply_vector_with_matrix(A:list, B:list[list], F_q:list) -> list:
    if len(A) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B.")
    
    result = [0] * len(B[0])

    # Perform the multiplication
    for j in range(len(B[0])):  # Loop through the columns of the matrix
        for i in range(len(A)):  # Loop through the elements of the vector
            result[j] += A[i] * B[i][j]

        result[j] = result[j] % len(F_q)
        
    return result


def text_to_vectors(text:str, F_q:list) -> list:
    result = []
    hashed_values = {}

    for c in text:
        ascii_digit = ord(c)

        if ascii_digit in hashed_values:
            encoded_c = hashed_values[ascii_digit]
        else:
            encoded_c = decimal_to_base(ascii_digit, len(F_q))
            if len(encoded_c) < 12:
                encoded_c = [0] * (12 - len(encoded_c)) + encoded_c

            hashed_values[ascii_digit] = encoded_c

        result.append(encoded_c)

    return result


def decimal_to_base(n:int, base:int) -> list:
    """Convert a decimal number to its representation in any base."""
    
    if n == 0:
        return [0]
    
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base

    digits.reverse()
    return digits


def base_to_decimal(num:list, base:int) -> int:

    decimal = 0
    for i, digit in enumerate(reversed(num)):
        decimal += digit * (base ** i)

    return decimal
