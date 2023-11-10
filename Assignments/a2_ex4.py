
num_lines = int(input("Enter number of lines: "))

if num_lines < 3:
    print("Invalid number of lines")
else:
    print("-" * num_lines)

    in_between_lines = num_lines - 2
    spaces = " " * (num_lines - 2)

    for _ in range(in_between_lines):
        print(f"|{spaces}|")

    print("-" * num_lines)
