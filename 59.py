def username_extractor(email):
    email_parts = email.split("@") #spliting on '@' to divide into two parts
    print(f"Username is {email_parts[0]}")
    print(f"Company is {email_parts[1]}")

email = input("Eneter your Email: ")
username_extractor(email)