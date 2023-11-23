import os

file = open("testfile.txt", "a")
file.write (input("Enter any text: "))
file.close()

def count_of_symbols(filename):
    print("Unique symbols and count: ")

    with open(filename, 'r') as file:
        content = file.read()
        unique_symbols = set(content)
        for char in unique_symbols:
            count = content.count(char)
            print(f"{char}: {count}", end=" ")



filename = ("testfile.txt")
count_of_symbols(filename)

os.remove("testfile.txt")