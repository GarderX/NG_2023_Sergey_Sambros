def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divis(a,  b):
    return a / b

def deegre(a, b):
    return a ** b

def sqrt(a):
   return a ** 0.5

while True:  
    print(" __________")
    vibiray = input("|calculator|\n|1: + |2: -|\n|3: * |4: /|\n|5: ^ |6: √|  ")
    if vibiray in ('1', '2', '3', '4', '5'):
       fnum = int(input("Enter first number: "))
       snum = int(input("Enter second number: "))
    else: fnum = int(input("Enter root of number: "))
#Zhmishenko Valeriy Albertovich blagoslovil etot calculator
    result = None

    match vibiray:
        case "1":
         result = add(fnum, snum)
        case "2":
         result = sub(fnum, snum)
        case "3":
         result = mult(fnum, snum)
        case "4":
         result = divis(fnum, snum)
        case "5":
         result = deegre(fnum, snum)
        case "6":
         result = sqrt(fnum)
    print ("Result: ", result)