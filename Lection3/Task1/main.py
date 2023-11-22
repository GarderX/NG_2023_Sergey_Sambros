file = open("testfile.txt", "a") # w - write, r - read, x - create, a - add to the end
file.write("Enter any text")
file.close()

def symbols(file):
 with open("testfile.txt", 'r') as file:
            content = file.read()
            character_count = {}
            for char in content:
                character_count[char] = character_count.get(char, 0) + 1

            return symbols
 
result = symbols(file)

