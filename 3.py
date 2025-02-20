n = int(input("Enter a number: "))
result = {}

# Generate the dictionary
for i in range(1, n + 1):
    result[i] = i * i

# Print the dictionary
print(result)
