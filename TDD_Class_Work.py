def testInput():
    text = input("Enter your text:\n")
    if (text.isalpha() == True):
        return text
    else:
        return False

def textFix(text):
    if (text.isalpha() == False):
        for i in range(len(text)):
            if 90 < ord(text[i]) < 97 or ord(text[i]) > 122:
                text = text.replace(chr(ord(text[i])), chr(ord(text[i]) - 26))
        return text

text = testInput()
if (text):
    for i in range(len(text)):
        text = text[:i] + chr(ord(text[i]) + 3) + text[i + 1:]
    text = textFix(text)
    print(text)
else:
    print("All characters in the text should be alphabets!")
