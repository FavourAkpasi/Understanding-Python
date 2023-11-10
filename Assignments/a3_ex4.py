user_string = input("Enter comma-separated elements: ")
user_string_list = user_string.split(",")
integers = []
rest = []
integers_dict = {}

for string in user_string_list:
    if string.isdecimal():
        integers.append(int(string))
    else:
        rest.append(string)

for integer in integers:
    occurrence = 0
    for i in range(len(integers)):
        if integer == integers[i]:
            occurrence += 1
    integers_dict[integer] = occurrence

print(f"integers: {integers} \ncounts: {integers_dict} \nrest: {rest}")
