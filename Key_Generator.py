from cryptography.fernet import Fernet

# Key generator function

def generate_key():
    key = Fernet.generate_key()
    with open("Encryption.Key", 'wb') as file:
        file.write(key)
print("Key has been saved successfully")

if __name__ == "__main__":
    generate_key()