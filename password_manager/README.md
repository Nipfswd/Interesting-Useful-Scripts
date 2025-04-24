# **CLI Password Manager**

## **Overview**
The CLI Password Manager is a lightweight and secure command-line tool for storing, retrieving, and generating passwords. Designed with encryption in mind, this tool ensures your sensitive data is safe and easily accessible. Its simplicity and practicality make it perfect for everyday password management tasks.

## **Key Features**
- **AES Encryption**: Encrypts and decrypts passwords using a passphrase for enhanced security.
- **Password Generation**: Generates secure passwords based on user-defined criteria (length, special characters, etc.).
- **Search Functionality**: Quickly retrieve credentials by service name.
- **JSON-Based Storage**: Encrypted passwords are stored in an organized JSON file.
- **Secure Master Passphrase**: Protects access to your credentials.

## **Folder Structure**
```plaintext
password_manager/
├── src/
│   ├── cli.py             # Command-line interface
│   ├── encryption.py      # Handles AES encryption/decryption
│   ├── storage.py         # Manages JSON-based storage
│   ├── generator.py       # Generates random secure passwords
├── tests/
│   ├── test_encryption.py # Unit tests for encryption functions
│   ├── test_storage.py    # Unit tests for file handling
└── README.md              # Documentation for setup and usage
