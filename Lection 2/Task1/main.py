spear = []
kilkist = int(input("How many elements do you want add to list? - "))
kil = 0
while kilkist > 0:   
  spear.append(input("Enter element: "))
  kil += 1
  if kilkist == kil:
    break
print("The list: ", spear)
usei = set(spear)
unil = list(usei)
print("The list with unique elements: ", unil)
