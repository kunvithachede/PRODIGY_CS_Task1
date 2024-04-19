def caesar_cipher(text, shift, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in text:
        if char in alphabet:  # only shift alphabetic characters
            old_index = alphabet.index(char)
            if direction == 'encrypt':
                new_index = (old_index + shift) % len(alphabet)
            else:  # decrypt
                new_index = (old_index - shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char  # non-alphabetic characters are not shifted

    return result

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    direction = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ")
    print(caesar_cipher(text, shift, direction))

if __name__ == "__main__":
    main()