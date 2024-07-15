# Encryption and Authentication Application

## Description
This project is a simple GUI application that allows users to authenticate themselves and perform encryption and decryption of messages using the Caesar cipher. It is built using Python and Tkinter and includes logging and security features.

## Features
- User authentication with a simple username and password database.
- Logging of suspicious login attempts.
- Caesar cipher encryption and decryption.
- User-friendly GUI with message boxes positioned on the right side of the screen.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Abubakker-98/Novanectar
    ```

2. Navigate to the project directory:
    ```bash
    cd Encryption-Authentication-App
    ```

3. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

4. Install the required libraries:
    ```bash
    pip install cryptography
    ```

## Usage

1. Run the `Task1.py` script:
    ```bash
   Task1.py
    ```

2. The GUI window will appear. Enter your username and password to log in.

3. After successful authentication, you can enter a message and a shift value to encrypt or decrypt the message using the Caesar cipher.

## Code Overview

- **Caesar Cipher Encryption/Decryption:** Functions `caesar_encrypt` and `caesar_decrypt` perform the encryption and decryption using a given shift value.
- **User Authentication:** Function `authenticate` checks the entered username and password against a simple database of users. Suspicious login attempts are logged.
- **Right Side Message Boxes:** Function `right_side_messagebox` displays message boxes on the right side of the screen.
- **GUI Setup:** The GUI is created using Tkinter, with login and encryption/decryption frames managed separately.



## Contributing

If you have suggestions for improving this project, feel free to fork the repository and create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding!
