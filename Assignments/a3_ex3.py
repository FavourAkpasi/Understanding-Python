user_string = input("Enter comma-separated elements: ")
user_string_list = user_string.split(",")
user_string_char_list = []
user_string_hash_dict = {}

# for i in range(len(user_string_list)):
#     for j in range(len(user_string_list[i].split())):
#         user_string_hash.append(ord(user_string_list[i][j]))
# print(user_string_list, user_string_hash)

for i in range(len(user_string_list)):
    for char in user_string_list[i]:
        user_string_char_list.append(char)

for i in range(len(user_string_char_list)):
    user_string_hash_dict[user_string_char_list[i]] = ord(user_string_char_list[i])

for word in user_string_list:
    final_hash = 0
    for char in word:
        final_hash += user_string_hash_dict[char]
    print(f"'{word}' -> {final_hash}")
