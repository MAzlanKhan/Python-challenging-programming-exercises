import math

# Fixed values 
C = 50
H = 30

D = input("Enter the values for D: ") #Taking Input

D_values = D.split(',') #Converting to List
print(f"Values are {D_values}")
# print(type(D_values))

for value in D_values: #Used For loops to use values in list one by one
    Int_D = int(value) #converting values in Integar
    Q = math.sqrt((2 * C * Int_D)/H)
    print(Q)