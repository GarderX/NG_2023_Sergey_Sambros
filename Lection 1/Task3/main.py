vibiray = input("choose 1 or 2 for convertation: \n1. Celsius to Farenheit \n2. Farenheit to Celsius\n")

if vibiray == "1":
         celsius = float(input("Enter celsius: "))
         fahrenheit = (celsius * 9/5) + 32
         print("Farenheit:", fahrenheit)
elif vibiray == '2':
        fahrenheit = float(input("Enter farenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Celsius:", celsius)
else:
        print("Enter 1 or 2!")