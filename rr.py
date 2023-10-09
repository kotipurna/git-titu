
n = 6  # Change this value to adjust the number of rows

# Outer loop for rows
for i in range(n):
    # Inner loop for columns
    for j in range(n - 1):
        # Print space or * based on conditions
        if j < i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    
    # Print the special character and a space
    print("@", end=" ")
    
    # Inner loop for columns (part 2)
    for j in range(n - 1, -1, -1):
        # Print $ or * based on conditions
        if j > i:
            print("$", end=" ")
        else:
            print("*", end=" ")
    
    # Move to the next line for the next row
    print()
