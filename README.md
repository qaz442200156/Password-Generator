# Password-Generator

# Auto User Password Generator

This Python script reads user data from a CSV file, generates passwords for users who don't have one, and writes the updated user data to a new CSV file. It also adds the new users to the system.

## Requirements

- Python 3
- The `secrets` and `csv` modules (included in standard Python installations)
- The `subprocess` and `pathlib` modules (included in standard Python installations)

## Usage

1. Prepare a CSV file with user data. The CSV file should have a header row with field names. The following field names are used by the script:

   - `username`: The user's username.
   - `password`: The user's password. If this field is empty for a user, the script will generate a password for them.
   - `real_name`: The user's real name.

2. Place the CSV file in the `data` directory and name it `users_in.csv`.

3. Run the script with Python 3:

   ```bash
   python3 AutoUserPasswordGenerator.py
   ```
4. The script will create a new CSV file in the data directory named users_out.csv. This file will contain the same user data as the input file, but with passwords filled in for all users.

5. The script will also add the new users to the system using the /sbin/useradd command. This requires superuser (root) privileges.

## Notes

- The script uses the secrets.token_hex(8) function to generate passwords. This function generates a secure random password with 16 hexadecimal characters.

- The script uses the utf-8-sig encoding to read and write CSV files. This encoding is compatible with UTF-8 and automatically removes the Byte Order Mark (BOM) if it's present.

# Password Generator

This Python script generates secure random passwords.

## Requirements

- Python 3
- The `secrets` module (included in standard Python installations)

## Usage

1. Run the script with Python 3:

   ```bash
   python3 PasswordGenerator.py
   ```
2. The script will prompt you to enter the length of the password you want to generate. Enter a positive integer.

3. The script will generate 11 passwords of the specified length and print them to the console.

## Notes

- The script uses the secrets.token_urlsafe function to generate passwords. This function generates a secure random URL-safe text string. If you want to generate hexadecimal or byte passwords, you can uncomment the corresponding lines in the code.

- The script will keep prompting for a password length until you enter a positive integer.