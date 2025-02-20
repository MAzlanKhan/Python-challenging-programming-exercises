list1 = list(range(0,21))
print(list1)

# using filter to make a list having even numbers 
newlist = list(filter(lambda x: x%2 == 0, list1))
print(newlist)