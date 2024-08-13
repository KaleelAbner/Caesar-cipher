def caesar_cipher(text, shift):
    result = ""
    
    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's neither uppercase nor lowercase, leave it unchanged
        else:
            result += char
            
    return result

# Example usage
plaintext = "Hello, World!"
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)