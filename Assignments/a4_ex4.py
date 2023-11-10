def round_(number, ndigits: int = None):
    if ndigits is None:
        return int(number)
    else:
        rounded_number = number * (10 ** ndigits)
        rounded_number = int(rounded_number + 0.5)
        return rounded_number / (10 ** ndigits)



# print(round_(777.7777, 3))
