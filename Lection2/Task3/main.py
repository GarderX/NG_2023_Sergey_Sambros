
num = int(input("Enter the number:  "))

list = []
for number in range(1, num + 1):
    chisla = [notete for notete in range(1, number + 1) if number % notete == 0]
    list.append([number, chisla])

print("---" * 41)

print("Numbers: ", end="")
for kilk in list:
    print(f"{kilk[0]},", end=" ")

simple_numbers = [kilk[0] for kilk in list if len(kilk[1]) == 2]
print("\n", "---" * 40,  (f"\nDeliteli: {kilk[1]}\n"), "---" * 40 )

print("Prostie chisla: ", simple_numbers, "\n", "---" * 40)
