list = []
elem = int(input("How many elements do you want add to list? - "))
el = 0
while elem > 0:   
  list.append(input("Enter element: "))
  el += 1
  if elem == el:
    break

print(list)
for x in list:
  if "a" in x:
    list.append(x)
print(list)

print(list)
count = len(list)
print("Количество элементов в списке:", count)