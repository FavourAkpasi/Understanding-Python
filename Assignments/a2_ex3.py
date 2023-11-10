
start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

even_count = 0
odd_sum = 0


current_number = start

for i in range(min(5, stop - start + 1)):
    print(f"Number in iteration {i} = {current_number}")
    if current_number % 2 == 0:
        even_count += 1
    else:
        odd_sum += current_number
    current_number += step


print(f"Even number count = {even_count}")
print(f"Sum of odd numbers = {odd_sum}")
