# Initializing Variables 
letters = 0
digits = 0

# Taking input 
data = input("Enter something: ")

# Using for loop 
for char in data:
    if char.isalpha(): # .isalpha() is a method
        letters += 1
    elif char.isdigit(): # .isdigit() is a method
        digits += 1
    else:
        print("Invalid input")
        
# output 
print(f"Number of Letters are {letters}")
print(f"Number of Digits are {digits}")