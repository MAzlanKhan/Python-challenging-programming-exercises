numbers = []

# Iterate through the range 2000 to 3200 (both inclusive)
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        numbers.append(str(num))

# Join the numbers with a comma and print
print(",".join(numbers))
