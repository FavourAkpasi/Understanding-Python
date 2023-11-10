# Read four numbers from the console
a = int(input("Enter a number for 'a': "))
b = int(input("Enter a number for 'b': "))
c = int(input("Enter a number for 'c': "))
d = int(input("Enter a number for 'd': "))

# Perform calculations and print results
print("The sum of a, b and d is:", a + b + d)
print("The product of all four numbers is:", a * b * c * d)
print("The sum of a and b times the sum of c and d is:", (a + b) * (c + d))
print("The result of an integer division when dividing a by d is:", a // d)
print("The result of a regular division when dividing a by d is:", a / d)
print("The remainder of a division (modulo) when dividing a by b is:", a % b)
print("c to the power of -a:", c ** (-a))
print("b to the power of 1/2 (square root):", b ** (1/2))
print("Complex equation:", (b / 3) * (b ** (a + d/2) - 1) + c)
