def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if not char.isalpha():
            result += char
            continue

        base = ord('a') if char.islower() else ord('A')
        result += chr((ord(char) - base + shift) % 26 + base)

    return result