
number_input = int(input("Enter the number:  "))

list = []
for digit in range(1, number_input + 1):
    numbers = [divisor for divisor in range(1, digit + 1) if digit % divisor == 0]
    list.append([digit, numbers])

print("---" * 41)

print("Numbers: ", end="")
for list_quantity in list:
    print(f"{list_quantity[0]},", end=" ")

simple_numbers = [list_quantity[0] for list_quantity in list if len(list_quantity[1]) == 2]
print("\n", "---" * 40,  (f"\nDeliteli: {list_quantity[1]}\n"), "---" * 40 )

print("Prostie chisla: ", simple_numbers, "\n", "---" * 40)
