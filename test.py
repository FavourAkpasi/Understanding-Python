# some_string = ""
# while True:
#     user_input = input(" word please ")
#     if user_input != "end":
#         some_string += user_input
#     else:
#         break
# print(some_string)


user_string = input("string? ")
num_of_digits = 0
num_of_lowercase_char = 0
num_of_special_characters = 0
for char in user_string:
    if char == char.lower() and char.isdigit() is False:
        num_of_lowercase_char += 1
    if char.isdigit():
        num_of_digits += 1

print(num_of_digits)
print(num_of_lowercase_char)
