vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
enter_string = input(str("Input text: "))
glasn = [char for char in enter_string if char in vowels]
print("Vowels in the string:", glasn)