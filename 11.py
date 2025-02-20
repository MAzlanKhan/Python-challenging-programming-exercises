numbers= input("Enter the numbers (Comma seperated): ") #taking input
numbers_list = numbers.split(",") #making list

for values in numbers_list: #USING for loop for each value of list
    int_values = int(values)
    if int_values % 5 == 0:
        print(int_values)
    