def pin(list):
 for num in list:
  if isinstance(num, (int, float)):
    print(num)

list = []
elem = int(input("How many elements do you want add to list? - "))
el = 0


while elem > 0:   
  list.append(input("Enter element: "))
  el += 1
  if elem == el:
    break
print(list)