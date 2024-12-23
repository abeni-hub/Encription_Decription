import string
import random

def generate_key():
    """
    Generates a random substitution cipher key.
    Returns:
        dict: Mapping of plain alphabet to cipher alphabet.
    """
    plain_alphabet = list(string.ascii_lowercase)
    cipher_alphabet = plain_alphabet[:]
    random.shuffle(cipher_alphabet)
    return dict(zip(plain_alphabet, cipher_alphabet))

def encrypt(text, key):
    """
    Encrypts a given text using a monoalphabetic substitution cipher.

    Args:
        text (str): The plaintext to be encrypted.
        key (dict): The substitution cipher key.

    Returns:
        str: The encrypted ciphertext.
    """
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char in key:
            encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    """
    Decrypts a given ciphertext using a monoalphabetic substitution cipher.

    Args:
        ciphertext (str): The text to be decrypted.
        key (dict): The substitution cipher key.

    Returns:
        str: The decrypted plaintext.
    """
    reverse_key = {v: k for k, v in key.items()}
    decrypted_text = ""
    for char in ciphertext:
        if char in reverse_key:
            decrypted_text += reverse_key[char]
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
if __name__ == "__main__":
    key = generate_key()
    print("Generated Key:", key)

    plaintext = "Hello World!"
    print("Plaintext:", plaintext)

    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
