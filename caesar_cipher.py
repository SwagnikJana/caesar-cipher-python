def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            # Handle lowercase letters
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            # Keep spaces, numbers and symbols unchanged
            result += char

    return result


print("===== Caesar Cipher =====")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1 or 2): ")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)

elif choice == "2":
    decrypted_message = caesar_cipher(message, -shift)
    print("Decrypted message:", decrypted_message)

else:
    print("Invalid choice!")