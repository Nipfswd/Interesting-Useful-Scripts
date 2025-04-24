import argparse
from src.encryption import Encryption
from src.storage import Storage
from src.generator import PasswordGenerator

def main():
    parser = argparse.ArgumentParser(description="CLI Password Manager")
    parser.add_argument("--passphrase", required=True, help="Passphrase to unlock the password manager")
    parser.add_argument("--add", action="store_true", help="Add a new password")
    parser.add_argument("--retrieve", help="Retrieve a password by service name")
    parser.add_argument("--generate", action="store_true", help="Generate a random password")
    parser.add_argument("--service", help="Service name (e.g., email, social)")
    parser.add_argument("--username", help="Username associated with the service")
    parser.add_argument("--notes", help="Optional notes")

    args = parser.parse_args()
    encryption = Encryption(args.passphrase)
    storage = Storage()

    if args.add:
        if not args.service or not args.username:
            print("Service and username are required to add an entry.")
            return
        password = input("Enter password: ")
        encrypted_password = encryption.encrypt(password)
        storage.add_entry(args.service, args.username, encrypted_password.hex(), args.notes or "")
        print(f"Password for {args.service} added successfully.")

    elif args.retrieve:
        entry = storage.get_entry(args.retrieve)
        if entry:
            decrypted_password = encryption.decrypt(bytes.fromhex(entry["password"]))
            print(f"Service: {args.retrieve}\nUsername: {entry['username']}\nPassword: {decrypted_password}\nNotes: {entry['notes']}")
        else:
            print(f"No entry found for service: {args.retrieve}")

    elif args.generate:
        generator = PasswordGenerator()
        print(f"Generated password: {generator.generate()}")

if __name__ == "__main__":
    main()
