import os

file = open("testfile.txt", "a")
file.write (input("Enter any text: "))
file.close()

def count_of_symbols(filename):
    print("Symbols and count: ")

    with open(filename, 'r') as file:
            symbols = {}
            content = file.read()
            for char in content:
                if char in symbols:
                    symbols[char] += 1
                else:
                    symbols[char] = 1

            print(symbols)

filename = ("testfile.txt")
count_of_symbols(filename)

os.remove("testfile.txt")
