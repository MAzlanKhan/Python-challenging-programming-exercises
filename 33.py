def print_square_dict():
    square_dict = {}

    # Populate the dictionary with keys and their squares as values
    for num in range(1, 4):  
        square_dict[num] = num ** 2

    print(square_dict)


print_square_dict()
