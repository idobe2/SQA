text = input("Enter your text:\n")
for i in range(len(text)):
    text = text[:i] + chr(ord(text[i])+3) + text[i+1:]
print(text)