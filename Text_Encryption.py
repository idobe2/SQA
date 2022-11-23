def test_input(new_text):  # Step 1: Test func for the input
    # new_text = input("Enter your text:\n")
    if type(new_text) not in [str]:
        raise TypeError('The provided value is not a string')
    if new_text.isalpha():
        return new_text
    else:
        return False


# Step 3: New function has been added to fix last letters encryption
def correction(en_text):
    if not en_text.isalpha():
        for c in range(len(en_text)):
            if 90 < ord(en_text[c]) < 97 or ord(en_text[c]) > 122:
                en_text = en_text.replace(chr(ord(en_text[c])), chr(ord(en_text[c]) - 26))
        return en_text


def encoding(text):
    if text:
        for i in range(len(text)):
            text = text[:i] + chr(ord(text[i]) + 3) + text[i + 1:]
        text = correction(text)
        print(text)
    else:
        print("All characters in the text should be alphabets!")
# Step 2: Run test function
