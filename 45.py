list1 = [1,2,3,4,5,6,7,8,9,10]

list_wo_even = list(filter(lambda x: x %2 != 0, list1))
print(list_wo_even)