list = []
elem = int(input("How many elements do you want add to list? - "))
el = 0
while elem > 0:   
  list.append(input("Enter element: "))
  el += 1
  if elem == el:
    break

count = sum(str(numbers).isdigit() for numbers in list)

print(list)

print("Count of number in list:", count)