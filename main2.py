# main.py
# Variables and Data Types
name = "Alice"                  # String type
age = 25                        # Integer type
height = 5.6                    # Float type
is_student = True               # Boolean type

# String Manipulation
greeting = f"Hello, {name}!"    # f-string for formatting
print(greeting.upper())         # Convert to uppercase: "HELLO, ALICE!"

# List Operations
fruits = ["apple", "banana"]
fruits.append("cherry")         # Add item to list
fruits.remove("apple")          # Remove item from list
print(f"Fruits: {fruits}")      # Output: ["banana", "cherry"]

# Conditional Logic
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"                 # This block executes
else:
    grade = "C"
print(f"Grade: {grade}")        # Output: B

# Looping Through Lists
numbers = [1, 2, 3]
squared = []
for num in numbers:
    squared.append(num ** 2)    # Append squared values
print(f"Squared: {squared}")    # Output: [1, 4, 9]

# List Comprehensions (compact loop)
cubed = [num ** 3 for num in numbers]
print(f"Cubed: {cubed}")        # Output: [1, 8, 27]