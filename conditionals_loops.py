"""
Understanding loops and conditionals.
Author - Akpasi Favour
modified Andreas Schörgenhumer's code from Programming in Python 1
"""

action = ""
while action.lower() != "exit":
    action = input("Please enter an action (must be one of "
                   "'sum', 'count', 'combinations', 'exit'): ")
    if action.lower() == "exit":
        print("exited")
        break
    elif action.lower() == "sum":
        n = int(input("Enter integer number > 0: "))
        if n > 0:
            sum_up_to_n = 0
            for x in range(n + 1):
                sum_up_to_n += x
            # Here, we can see an assertion. Since we know that "n" is > 0, the
            # sum of all numbers up to "n" (inclusive) must also be > 0, which
            # is exactly what we integrate here as a short sanity check. If the
            # assertion fails, we immediately know that we made a mistake.
            assert sum_up_to_n > 0
            print(f"Sum up to {n} = {sum_up_to_n}")
        else:
            print(f"Action failed: {n} is not > 0")
    elif action.lower() == "count":
        word = input("Enter word: ")
        char_to_count = input(f"Enter character to count in '{word}': ")
        count = 0

        for char in word:
            if char == char_to_count:
                count += 1

        print(f"Character '{char_to_count}' occurred {count} times in '{word}'")
    elif action.lower() == "combinations":
        n1 = int(input("Enter first integer number: "))
        n2 = int(input("Enter second integer number: "))

        for i1 in range(n1):
            for i2 in range(n2):
                print(f"{i1:3d} {i2:3d}")
    else:
        print(f"Unknown action '{action}'")
