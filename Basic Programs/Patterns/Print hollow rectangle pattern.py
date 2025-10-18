# Print Hollow Rectangle Pattern

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nHollow Rectangle Pattern:\n")

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        # Print * at border positions, space inside
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to next line
