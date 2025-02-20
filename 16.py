# taking input 
numbers = input("Enter the numbers (Commas seperated): ")
numbers_list = numbers.split(",") #making list

#using for loop for each value
for values in numbers_list:
    int_values = int(values)
    if int_values % 2 != 0: #farmula for odd numbers (ofcrs non-evens are odds)
        print(int_values ** 2)
        
        