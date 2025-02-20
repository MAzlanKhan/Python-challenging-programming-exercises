words = input("Enter the words (Commas seperated): ") #Taking Input
wordsset = set(words.split(",")) #making the set
print(f"Original Set is: {wordsset}") #sorting the set
print(f"Sorted Set is: {sorted(wordsset)}") #sorting the set
