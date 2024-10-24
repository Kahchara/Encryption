import argparse
from cryptography.fernet import Fernet
import os

# Function to load in a key generated by "Key_Generator.py"
def load_key():
    try:
        with open("Encryption.Key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print(f"Encryption.key could not be found")
        exit(1)

#--------------------------------------------------------------------------------------------------------
# Function to encrypt a file
def encrypt_file(filename, key):
    fernet = Fernet(key)

    if not os.path.exists(filename):
        print(f"A file with the name {filename} could not be found")
        return
    
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
    
        with open(filename + ".encrypted", "wb") as file:
            file.write(encrypted_data)
    
        print(f"{filename} has been encrypted.")

    except Exception as e:
        print(f'An unexpetected error has occured while attempting to encrypt {filename}: {e}')

#--------------------------------------------------------------------------------------------------------
# Function to decrypt a file
def decrypt_file(filename, key):
    fernet = Fernet(key)
    
    if not os.path.exists(filename):
        print(f"A file with the name {filename} could not be found")
        return
    
    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()
    
        decrypted_data = fernet.decrypt(encrypted_data)
    
        with open(filename.replace(".encrypted", ".decrypted"), "wb") as file:
            file.write(decrypted_data)
    
        print(f"{filename} has been decrypted.")
    except Exception as e:
        print (f'An unexpetected error has occured while attempting to decrypt {filename}: {e}')

#--------------------------------------------------------------------------------------------------------
# Main function to encrypt and decrypt
def main():
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt a file.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="State whether you would like to encrypt or decrypt a file.")
    parser.add_argument("filename", help="Name of the file to be encrypted or decrypted.")
    
    args = parser.parse_args()
    
    key = load_key()
    
    if args.mode == "encrypt":
        encrypt_file(args.filename, key)
    elif args.mode == "decrypt":
        decrypt_file(args.filename, key)

if __name__ == "__main__":
    main()
