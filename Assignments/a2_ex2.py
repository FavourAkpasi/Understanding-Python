previous_digit = None

while True:
    user_input = input("Enter number or 'x': ")

    if user_input == 'x':
        if previous_digit is None:
            print("Empty sequence")
        else:
            print("All numbers had the same digit in the ones place")
        break

    if user_input.isdigit():
        current_digit = int(user_input) % 10

        if previous_digit is not None and current_digit != previous_digit:
            print(f"{current_digit} and {previous_digit} differ in the ones place")
            break
        previous_digit = current_digit
    else:
        print("Invalid input. Please enter a positive integer or 'x'")
