import base64

def encrypt_message(message):
    encoded = base64.b64encode(message.encode())
    return encoded.decode()

def decrypt_message(encoded_message):
    decoded = base64.b64decode(encoded_message.encode())
    return decoded.decode()

while True:
    print("\n===== Cryptographic Chat Application =====")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter message: ")
        encrypted = encrypt_message(message)
        print("Encrypted Message:", encrypted)

    elif choice == "2":
        encrypted_message = input("Enter encrypted message: ")
        try:
            decrypted = decrypt_message(encrypted_message)
            print("Decrypted Message:", decrypted)
        except:
            print("Invalid encrypted message!")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")