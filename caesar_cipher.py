# Caesar Cipher Implementation

def caesar_cipher(text, shift, mode):
    result = ""
    
    for char in text:
        if char.isalpha():
            # Check uppercase or lowercase
            start = 65 if char.isupper() else 97
            
            if mode == "E":  # Encrypt
                result += chr((ord(char) - start + shift) % 26 + start)
            elif mode == "D":  # Decrypt
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char  # keep spaces and symbols as is
    
    return result


# Main Program
message = input("Enter message: ")
shift = int(input("Enter shift value: "))
mode = input("Enter E for Encrypt or D for Decrypt: ").upper()

output = caesar_cipher(message, shift, mode)
print("Result:", output)