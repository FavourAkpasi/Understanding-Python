# Read the number of ordered items from the console
num_cables = int(input("Enter the number of ordered cables: "))
num_monitors = int(input("Enter the number of ordered monitors: "))
num_keyboards = int(input("Enter the number of ordered keyboards: "))

# Define the prices
price_cable = 9.90
price_monitor = 249.99
price_keyboard = 27.50

# Calculate the total cost for each item
total_cables = num_cables * price_cable
total_monitors = num_monitors * price_monitor
total_keyboards = num_keyboards * price_keyboard

# Calculate the total cost of the entire order
total_order = total_cables + total_monitors + total_keyboards

# Print the order form
print("==================================================")
print("PC Parts Store - Order")
print("==================================================")
print(f"Number of cables: {num_cables:3}")
print(f"Number of monitors: {num_monitors:3}")
print(f"Number of keyboards: {num_keyboards:3}")
print(f"{num_cables:3} cables ({price_cable:.2f} EUR each) = {total_cables:.2f} EUR")
print(f"{num_monitors:3} monitors ({price_monitor:.2f} EUR each) = {total_monitors:.2f} EUR")
print(f"{num_keyboards:3} keyboards ({price_keyboard:.2f} EUR each) = {total_keyboards:.2f} EUR")
print("--------------------------------------------------")
print(f"Total: {total_order:.2f} EUR")
print("==================================================")
