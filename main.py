# main.py
# 1. Variables and Data Types
name = "Furkan"
age = 30
weigh = 92.3
heigh = 179
is_student = True

print(f"Name: {name}, Age: {age}, Weigh: {weigh}, Heigh: {heigh}, Student: {is_student}")

# Functions
def greet(name):
    return f"Hello, {name}"

print(greet("Hong"))
# main.py
# Lists and Loops
fruits = ["apple", "banana", "cherry"]

print("Fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Dictionaries
person = {
    "name":"Betul",
    "age": 29,
    "is_student": False
}    

print(f"\nPerson Info:")
for key, value, in person.items():
    print(f"{key}:{value}")
