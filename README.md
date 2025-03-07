# Git and Python Learning Guide

* Scenario: Collaborative Python Project
* Project Name: python-learning-project
* Branches: main, person1, person2
* Goal: Create a Python script (main.py) with fundamental Python concepts.
* Collaboration Workflow: Person1 and Person2 work on separate branches, commit changes, and merge into main.

## Step 1: Initialize the Project
1.1 Create a New Repository
```
mkdir python-learning-project   //Creates a new directory.
cd python-learning-project      //Changes to the directory.
git init                        //Initializes a new Git repository.
```

## Step 2: Create main Branch
### 2.1 Add Basic Python Script
```
touch main.py                    // Creates an empty file.
git add main.py                  // Stages the file for commit.
git commit -m "Create main.py"   // Saves the file to the repository.
```

## Step 3: Person1’s Work (Branch person1)
### 3.1 Variables, Strings, and Lists
```
git checkout -b person1                             //Creates and switches to a new branch.
git add main.py                                    
git commit -m "Add variables, strings, and lists"
```


```
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
```


### 3.2 Conditional Statements
```
# Conditional Logic
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"                 # This block executes
else:
    grade = "C"
print(f"Grade: {grade}")        # Output: B
```
```
git add main.py
git commit -m "Add conditional statements"
```

### 3.3 Loops and List Methods
```
# Looping Through Lists
numbers = [1, 2, 3]
squared = []
for num in numbers:
    squared.append(num ** 2)    # Append squared values
print(f"Squared: {squared}")    # Output: [1, 4, 9]

# List Comprehensions (compact loop)
cubed = [num ** 3 for num in numbers]
print(f"Cubed: {cubed}")        # Output: [1, 8, 27]
```

```
git add main.py
git commit -m "Add loops and list methods"
```

## Step 4: Person2’s Work (Branch person2)
### 4.1 Dictionaries and Error Handling
```
# Dictionaries (key-value pairs)
person = {
    "name": "Bob",
    "age": 30,
    "is_student": False
}
print(person.get("name"))       # Output: Bob

# Error Handling with try-except
try:
    age_input = input("Enter your age: ")
    age = int(age_input)        # May raise ValueError
except ValueError:
    print("Invalid age!")       # Handles non-integer input
```
```
git checkout -b person2
git add main.py
git commit -m "Add dictionaries and error handling"
```

### 4.2 File Operations
```
# Writing to a File
with open("data.txt", "w") as file:
    file.write("Hello, World!") # Creates/overwrites data.txt

# Reading from a File
try:
    with open("data.txt", "r") as file:
        content = file.read()
    print(f"File content: {content}")  # Output: Hello, World!
except FileNotFoundError:
    print("File not found!")
```
```
git add main.py
git commit -m "Add file operations"
```

### 4.3 String Slicing and Methods
```
# String Slicing
text = "Python is fun!"
print(text[0:6])                # Output: Python
print(text.split())             # Split into list: ["Python", "is", "fun!"]

# String Methods
message = "  hello world  "
clean_message = message.strip().capitalize()
print(clean_message)            # Output: Hello world
```
```
git add main.py
git commit -m "Add string slicing and methods"
```

## Step 5: Merge Branches into main
### 5.1 Merge person1 into main
```
git checkout main      //Change working branch
git merge person1      //Combines changes from one branch into another.
```

### 5.2 Merge person2 into main
```
git merge person2
Final main.py After Merging
python
Copy
# Variables, Strings, and Lists
name = "Alice"
age = 25
height = 5.6
is_student = True

greeting = f"Hello, {name}!"
print(greeting.upper())

fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.remove("apple")
print(f"Fruits: {fruits}")

# Conditional Statements
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Grade: {grade}")

# Loops and List Methods
numbers = [1, 2, 3]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(f"Squared: {squared}")

cubed = [num ** 3 for num in numbers]
print(f"Cubed: {cubed}")

# Dictionaries and Error Handling
person = {
    "name": "Bob",
    "age": 30,
    "is_student": False
}
print(person.get("name"))

try:
    age_input = input("Enter your age: ")
    age = int(age_input)
except ValueError:
    print("Invalid age!")

# File Operations
with open("data.txt", "w") as file:
    file.write("Hello, World!")

try:
    with open("data.txt", "r") as file:
        content = file.read()
    print(f"File content: {content}")
except FileNotFoundError:
    print("File not found!")

# String Slicing and Methods
text = "Python is fun!"
print(text[0:6])
print(text.split())

message = "  hello world  "
clean_message = message.strip().capitalize()
print(clean_message)

```

```
git remote add origin https://github.com/.../....git    //Links your local repo to GitHub.
git push -u origin main                                 // Uploads your code to GitHub.
```

# Git Command Summary
## Command	Explanation
* **git init**                      : Creates a new Git repository.
* **git checkout -b <branch>**	    : Creates and switches to a new branch.
* **git add <file>**	            : Stages changes for the next commit.
* **git commit -m "message"**	    : Saves changes with a descriptive message.
* **git merge <branch>**	        : Combines changes from one branch into another.
* **git push origin <branch>**	    : Uploads local commits to a remote repository (e.g., GitHub).
         
# Key Python Concepts Covered
         
1. Variables & Data Types: Strings, integers, floats, booleans.

2. String Manipulation: upper(), strip(), split(), slicing, f-strings.

3. Lists & Methods: append(), remove(), list comprehensions.

4. Conditionals: if-elif-else logic.

5. Loops: for loops, iterating over lists.

6. Dictionaries: Key-value pairs, get() method.

7. Error Handling: try-except blocks.

8. File Operations: Reading/writing files with open().
