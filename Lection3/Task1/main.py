filename = input("Enter the name of the file you want to open: ")

def count_of_symbols(filename):
    print("Unique symbols and count: ")
 
    with open(filename, 'r') as file:
        content = file.read()
        unique_symbols = set(content)
        for char in unique_symbols:
            count = content.count(char)
            print(f"{char}: {count}", end=" ")

filename = (filename)
count_of_symbols(filename)