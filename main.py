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
