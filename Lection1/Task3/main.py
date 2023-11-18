def farenheit(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius

def celsius(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

while True:  
    choice = input("\n1. Farenheit to celsius \n2. Celsius to farenheit \nChoose 1 or 2: ")
    if choice in ('1'):
     farnum = float(input("Farenheit: "))
    else: celnum = float(input("Celsius: "))
    
    result = None

    match choice:
        case "1":
         result = farenheit(farnum)
         print("Celsius:", result)
        case "2":
         result = celsius(celnum)
         print("Farenheit:", result)
