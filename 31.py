s1 = input("Enter the sentemce: ")
s2 = input("Enter the sentemce: ")

if len(s1) > len(s2):
    print(f"{s1} is is Greater in Length.")
elif len(s2) > len(s1):
    print(f"{s2} is is Greater in Length.")
else:
    print(f"Both {s1} and {s2} are equal in Length.")
