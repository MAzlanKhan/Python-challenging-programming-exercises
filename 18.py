# PROGRAM Username and password to register
# Define Valid Password function to store Data 

def valid_password(x):
    lowerChars = "abcdefghijklmnopqrstuvwxyz"
    upperChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"
    symbols = "!@#$%^&*()_+`~|\.<>,?"

    # Check if password length is greater than 6
    if len(x) >= 6:
        # Check for presence of each type of character in password
        if (any(c in lowerChars for c in x) and
            any(c in upperChars for c in x) and
            any(c in digits for c in x) and
            any(c in symbols for c in x)):
            print("Valid Password")
        else:
            print("Invalid Password: Missing required character type.")
    else:
        print("Invalid Password: Password length should be at least 6.")

# Define User Data function to store Data 
def user_data(x,y):
    data= {x:y}
    print(data)

username = input("Enter Username: ")
password = input("Enter the Password: ")

# Calling Functions 
valid_password(password)
user_data(username,password)

