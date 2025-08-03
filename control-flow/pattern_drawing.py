# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to handle rows
while row < size:
    # Use for loop to handle columns (print starts)
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1