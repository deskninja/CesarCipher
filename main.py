alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    cipher_text = []

    for letter in text:
        shifted_index = (alphabet.index(letter) + shift) % (len(alphabet))
        cipher_text.append(alphabet[shifted_index])

    return ''.join(cipher_text)


def decrypt(text, shift):
    plaintext = []

    for letter in text:
        shifted_index = (alphabet.index(letter) - shift + len(alphabet)) % len(alphabet)
        plaintext.append(alphabet[shifted_index])

    return ''.join(plaintext)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'both' to encrypt and decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encrypt':
        print(encrypt(text, shift))
    elif direction == 'decrypt':
        print(decrypt(text, shift))
    elif direction == 'both':
        print(decrypt(encrypt(text, shift), shift))
