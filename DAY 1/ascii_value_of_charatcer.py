text = input("Enter a String-: ")
text_length = len(text)
print("ALPHABET\tASCII")
for char in text:
    ascii = ord(char)
    print(char, "\t\t\t", ascii)
