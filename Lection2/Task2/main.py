list = []
input_element = int(input("How many elements do you want add to list? - "))
element_in_the_list = 0
while input_element > 0:   
  list.append(input("Enter element: "))
  element_in_the_list += 1
  if input_element == element_in_the_list:
    break

count = sum(str(numbers).isdigit() for numbers in list)

print(list)

print("Count of number in list:", count)