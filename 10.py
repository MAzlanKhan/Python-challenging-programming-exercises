lines = input("Enter the sentence: ") #taking input
words = lines.split() #spliting sentence into words
unique_words = set(words) #making the set of words
print(sorted(unique_words)) #printing sorted set
