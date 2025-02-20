sentence = input("Enter something: ") # Taking input

# initializing variables 
UpperCase = 0
LowerCase = 0

# using for loop
for char in sentence:
    if char.isupper(): # isupper() is a method
        UpperCase +=1
    elif char.lower(): # islower() is a method
        LowerCase += 1
    else:
        print("Invalid input")

# output
print(f"Number of Upper-case chars are {UpperCase}")
print(f"Number of Lower-case chars are {LowerCase}")