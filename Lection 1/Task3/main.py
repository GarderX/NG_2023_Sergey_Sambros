def ctof(celsius):
    return (celsius * 9/5) + 32
def ftoc(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Choose type of convertation:")
print("1. Celsius to Farenheit")
print("2. Farenheit to Celsius")
while True:
    vibiray = input("choose 1 or 2 for convertation: ")

    if vibiray in ('1', '2'):
        if vibiray == '1':
            celsius = float(input("Enter celsius: "))
            fahrenheit = ctof(celsius)
            print("Farenheit:", fahrenheit)
        elif vibiray == '2':
            fahrenheit = float(input("Enter farenheit: "))
            celsius = ftoc(fahrenheit)
            print("Celsius:", celsius)