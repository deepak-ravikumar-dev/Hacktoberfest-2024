# Function to transpose a matrix
def transpose_matrix(matrix):
    # Use list comprehension to transpose the matrix
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix
result = transpose_matrix(matrix)

# Print the transposed matrix
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in result:
    print(row)
