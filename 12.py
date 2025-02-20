numbers = input("Enter numbers (seperated by commas): ") #taking input
numbers_list = numbers.split(",") #making list

for values in numbers_list: #using for loop to check each value
    int_numbers_list = int(values)
    if int_numbers_list % 2 == 0: 
        print(int_numbers_list)