
all_elements = []
unique_elements = []

while True:
    element = input("Enter element or 'x' when done: ")
    if element == 'x':
        break
    all_elements.append(element)
    if element not in unique_elements:
        unique_elements.append(element)
        unique_elements.sort()

print(f"all: {all_elements}")
print(f"unique (sorted): {unique_elements}")
