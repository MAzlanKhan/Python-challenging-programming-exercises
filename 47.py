list1 =[1,2,3,4,5,6,7,8,9,10]
newlist = list(map(lambda x: x**2 , list1))
# print(newlist)


# making a new list 
finallist = list(filter(lambda x: x %2 == 0, newlist))
print(finallist)