
# 🔐 Caesar Cipher Tool – Python Encryption & Decryption

A simple **Caesar Cipher** tool in Python that allows you to **encrypt and decrypt messages** using a shift-based substitution method. You can process messages directly in the console or read/write them from text files.

---

## ⚙️ Features

- Encrypt plain text messages using the Caesar Cipher  
- Decrypt encrypted messages to retrieve the original text  
- Supports uppercase and lowercase letters  
- Preserves spaces, punctuation, and special characters  
- Encrypt/decrypt messages from console input or files  
- Saves file results automatically to `results.txt`  

---

## 📝 How It Works

1. **Encryption:** Each letter is shifted by a user-specified number (`shift`) down the alphabet. Letters at the end wrap around.  
2. **Decryption:** The shift is reversed to retrieve the original message.  
3. Non-alphabetic characters (spaces, punctuation, numbers) remain unchanged.  

**Example:**

```

Plain text: HELLO WORLD
Shift: 3
Encrypted: KHOOR ZRUOG
Decrypted: HELLO WORLD

````

---

## 🚀 Usage

### 1. Run the Program

```bash
python caesar_cipher.py
````

### 2. Follow Console Prompts

* Choose whether to **encrypt (E)** or **decrypt (D)**
* Choose data source: **Console (C)** or **File (F)**
* Enter your message (or file path) and shift number (0–25)
* View encrypted/decrypted message or check the `results.txt` file for output

---

### 3. Example Console Flow

```
Welcome to the Caesar Cipher
This program encrypts and decrypts text with the Caesar Cipher.

Would you like to encrypt (e) or decrypt (d)?: e
Would you like to read from a file (f) or the console (c)?: c
What message would you like to encrypt: HELLO WORLD
What is the shift number (0-25): 3
Result: KHOOR ZRUOG
```

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:** Standard Python (no external dependencies)

---

## 👨‍💻 Author

**Suraj Poddar**

---

## 🔑 Alternative Names

* **Shift Cipher** – focuses on the letter shift
* **ROT-N** – rotational cipher, e.g., ROT13
* **Alphabetic Shift** – highlights letter transformation
* **Monoalphabetic Cipher** – single alphabet substitution

---

## 📄 License

This project is licensed under the **MIT License** – see the LICENSE file for details.

```

---

✅ **Why this README is professional:**

- Clear **project description** and purpose  
- **Step-by-step usage instructions** for beginners  
- **Examples** included for instant understanding  
- **Features and tech stack** listed for clarity  
- **Alternative terminology** to show awareness of cryptography standards  


