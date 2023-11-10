boolean = True
integer = 1
floating_point = 1.5
string = "hello"

print(f"{boolean}")
print(f"{integer:05}")  # minimum width of 5, with leading zeros
print(f"{floating_point:10.3f}")  # minimum width of 10, with 3 decimal places
print(f"{string * 3}")  # print string three times