import string


def shift_letters(text):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = chr((ord(char) - base + 3) % 26 + base)
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)
text = input('Введите строку: ')
text_shift = shift_letters(text)
print(text_shift)