def testInput():
    text = input("Enter your text:\n")
    if (text.isalpha() == True):
        return text
    else: return False

text = testInput()
if (text):
    for i in range(len(text)):
        text = text[:i] + chr(ord(text[i])+3) + text[i+1:]
    print(text)