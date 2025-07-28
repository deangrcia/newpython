def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def decrypt(cipher, shift):
    return encrypt(cipher, -shift)

while True:
    print("\n--- Caesar Cipher ---")
    choice = input("Choose [E]ncrypt, [D]ecrypt, or [Q]uit: ").strip().upper()

    if choice == "Q":
        break
    elif choice not in ["E", "D"]:
        print("Invalid option. Try again.")
        continue

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift (e.g. 3): "))
    except ValueError:
        print("Shift must be a number.")
        continue

    if choice == "E":
        result = encrypt(message, shift)
        print(f"Encrypted: {result}")
    elif choice == "D":
        result = decrypt(message, shift)
        print(f"Decrypted: {result}")
