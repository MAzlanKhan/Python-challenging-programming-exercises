def divide_by_zero():
    try:
        result = 5 / 0  # This will raise a ZeroDivisionError
        return result
    except ZeroDivisionError as e:
        print(f"WT**** Hereeee is yooouuurrr ERRRROOORRRRR BROOOOOOOOO!!!!!!!!  {e}")

# Calling the function
divide_by_zero()
