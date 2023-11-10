
duration = int(input("Please enter the duration of your subscription (in months): "))

if duration <= 0:
    print("Invalid subscription duration")
    exit(0)


if duration < 6:
    monthly_price = 6.50
elif duration < 12:
    monthly_price = 5.90
else:
    postal_code = input("Please enter your 4-digit postal code: ")

    if not postal_code.isdigit() or len(postal_code) != 4:
        print("Invalid postal code")
        exit(0)

    middle_digits = int(postal_code[1:3])
    monthly_price = 4 * middle_digits


total_price = monthly_price * duration


print(f"The price per month is {monthly_price:.2f}")
print(f"The full price for {duration} months is {total_price:.2f}")
