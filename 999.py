def divide_by_zero():
    try:
        result = 5 / 0  # This will raise a ZeroDivisionError
        return result
    except ZeroDivisionError as efg:
        print(f"Here is yooouuurrr ERRRROOORRRRR {efg}")

# Calling the function
divide_by_zero()
