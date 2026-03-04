
"""
Caesar Cipher Tool
To encrypt and decrypt the text
"""
import os

def welcome():
    """Greet the user and explain the tool."""
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

def enter_message(str_mode):
    """Get the message and shift number from user input."""
    if str_mode == "E":
        str_prompt = "What message would you like to encrypt: "
    else:
        str_prompt = "What message would you like to decrypt: "
    
    str_input_message = input(str_prompt).upper()

    while True:
        try:
            int_shift = int(input("What is the shift number (0-25): "))
            if 0 <= int_shift <= 25:
                return str_input_message, int_shift
            print("Shift number should be between 0-25! Try Again.")
        except ValueError:
            print("Please input an integer.")

def encrypt(str_text, int_shift):
    """Shift letters forward to hide the message."""
    str_result = ""
    for char_letter in str_text:
        if char_letter.isalpha():
            # We add the shift, then use modulo 26 to ensure the shift wraps
            int_alphabet_pos = (ord(char_letter) - 65 + int_shift) % 26
            str_result += chr(int_alphabet_pos + 65)
        else:
            # Non-alphabet characters (spaces, punctuation) are kept as-is.
            str_result += char_letter
    return str_result

def decrypt(str_text, int_shift):
    """Shift letters backward to read the message."""
    str_result = ""
    for char_letter in str_text:
        if char_letter.isalpha():
            # Similar to encryption, but we subtract the shift.
            int_alphabet_pos = (ord(char_letter) - 65 - int_shift) % 26
            str_result += chr(int_alphabet_pos + 65)
        else:
            str_result += char_letter
    return str_result

def process_file(str_filename, str_mode, int_shift):
    """Read file lines and process them."""
    list_processed_lines = []
    try:
        with open(str_filename, "r") as file_input:
            for str_line in file_input:
                # Remove trailing newlines and convert to uppercase for consistency.
                str_clean_line = str_line.strip().upper()
                # Only process lines that contain text.
                if str_clean_line:
                    if str_mode == "E":
                        list_processed_lines.append(encrypt(str_clean_line, int_shift))
                    else:
                        list_processed_lines.append(decrypt(str_clean_line, int_shift))
        return list_processed_lines
    except FileNotFoundError:
        print(f"Error: The file '{str_filename}' was not found.")
        return []

def is_file(str_filename):
    """Check if the file exists on the computer."""
    return os.path.isfile(str_filename)

def write_message(list_messages):
    """Save results into a text file."""
    try:
        with open("results.txt", "w", encoding="utf-8") as file_output:
            file_output.write("\n".join(list_messages))
        print("Output written to results.txt")
    except IOError as e:
        print(f"Error writing to file: {e}")

def message_or_file():
    """Ask user for the mode and data source."""
    while True:
        str_mode = input("Would you like to encrypt (e) or decrypt (d)?: ").upper()
        if str_mode in ("E", "D"):
            break
        print("Invalid Mode! Please enter 'e' or 'd'.")

    while True:
        str_source = input("Would you like to read from a file (f) or the console (c)?: ").upper()
        if str_source == "C":
            return str_mode, "C", None
        if str_source == "F":
            str_filename = input("Enter a file name: ")
           # Keep asking until a valid file is located on the disk.
            while not is_file(str_filename):
                str_filename = input("File doesn't exist! Enter a valid filename: ")
            return str_mode, "F", str_filename
        print("Invalid Source! Try again.")

def main():
    """Control the main program flow."""
    welcome()
    while True:
        # Get user choices from the selection function
        list_user_choices = message_or_file()
        str_mode = list_user_choices[0]
        str_source = list_user_choices[1]
        str_filename = list_user_choices[2]

        if str_source == "C":
            str_msg, int_shift = enter_message(str_mode)
            if str_mode == "E":
                print(f"Result: {encrypt(str_msg, int_shift)}")
            else:
                print(f"Result: {decrypt(str_msg, int_shift)}")
        else:
            # Handle shift input for file processing
            while True:
                try:
                    int_shift = int(input("What is the shift number (0-25): "))
                    if 0 <= int_shift <= 25:
                        break
                    print("Shift number should be between 0-25! Try Again.")
                except ValueError:
                    print("Please input an integer.")

            list_results = process_file(str_filename, str_mode, int_shift)
            if list_results:
                write_message(list_results)

        while True:
            str_choice = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if str_choice in ('y', 'n'):
                break
            print("Invalid input.")
            
        if str_choice == 'n':
            print("Thanks for using the program! Goodbye!")
            break

main()
