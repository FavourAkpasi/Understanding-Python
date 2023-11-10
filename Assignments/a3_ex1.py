
while True:
    try:
        rows = int(input("Number of rows: "))
        columns = int(input("Number of cols: "))
        break
    except ValueError:
        print("Please enter a valid number")


# Create the matrix with the specified format
matrix = [[1 if i == j else 0 for j in range(columns)] for i in range(rows)]

# Print the matrix with the desired formatting
print("   ", end="")
for j in range(columns):
    print(f"{j} ", end="")
print()
print(" ", "-" * (columns * 2))

for i in range(rows):
    print(f"{i}|", end=" ")
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
