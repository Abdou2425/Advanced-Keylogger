# 🖥️ Advanced Python Keylogger  
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-20232A?style=for-the-badge&logo=lets-encrypt&logoColor=yellow)
![Email](https://img.shields.io/badge/SMTP_Email-000000?style=for-the-badge&logo=gmail&logoColor=red)

## 📌 Overview  
This project is a **Third-year Python module assignment** designed to help students understand how monitoring tools function internally so they can better **defend themselves from untrusted or malicious software**.

The application is an **advanced keylogger**, built using Python, capable of collecting various activity logs and securely storing them inside a folder named **`files/`**, with an optional encryption step and automatic **email delivery** of the results.

> ⚠️ **This project is for ethical and educational purposes only.**  
Misuse of this tool can be illegal. The intent is to demonstrate how such tools work to improve cybersecurity awareness.

---

## 🎯 Features

### ⌨️ Keystroke Logging  
- Captures all user keystrokes in real-time  
- Saves them inside the `files/keystrokes.txt` log file  

### 📋 Clipboard Monitoring  
- Logs all copied text from the system clipboard  
- Stored in `files/clipboard.txt`  

### 🖼️ Screen Captures  
- Takes periodic screenshots  
- Saves them as image files inside the `files/` directory  

### 🎤 Microphone Audio Recording  
- Records microphone audio for a set duration  
- Stores recordings as `.wav` files  

### 🌐 Network Interface Enumeration  
- Lists available network adapters  
- Logs IP configuration and interface details  

### 💻 System Information Extraction  
- Collects machine metadata such as:  
  - OS version  
  - CPU details  
  - Hostname  
  - RAM info  
  - Boot time  

### 📬 Email Reporting  
- After all operations finish, the program sends collected logs to a configured email  
- Uses Python's SMTP library  

### 🔐 Cryptography Module  
Stored in `cryptography/`, allowing you to:  
- Generate encryption keys  
- Encrypt all data inside the `files/` directory  
- Strengthen security of stored logs  

---
## 🛠️ Tech Stack

### **Language**
- Python 3.x
### **Libraries Used**  
All dependencies are listed in `requirements.txt` 
## 📦 Project Structure
📂 Project/
│── Keylogger.py
│── requirements.txt
│── .env.example → use this to install your .env file
│── 📂 → this folder contain all the function that used in keylogger.py file
│── 📂 files/ → stores logs, screenshots, audio, etc.
│── 📂 cryptography/ → key generator + encryption utilities

## 🛠️ Setup & Configuration
Follow these steps to correctly configure and run the project on your local machine.

---

### 🔹 Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment support (`venv`)
- Email credentials for SMTP configuration

---
1. Clone the repository:
    ```bash
    git clone https://github.com/Abdou2425/Advanced-Keylogger.git
    cd Advanced-Keylogger
    ```
2. Create virtuel environment:
    ```bash
    python -m venv venv 
    ```
3. Activate your venv (windows version):
    ```bash
    venv\Scripts\activate 
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
        ```
5. Configure your nvironment variables and fill it with your data:
    ```bash
    mv .env.example .env
    ```
## ▶️ How to Run the Project

This project provides multiple execution options depending on the functionality you want to use.

---

### 🔹 1. Run the Main Program (Keylogger)

Running `Keylogger.py` will start the **entire monitoring system**.

```bash
python Keylogger.py
```
- When run it , This programe will:
- Capture keystrokes
- Log clipboard contents
- Record microphone audio
- Take screenshots
- Extract system and network information
- Store all collected data inside the files/ directory
- Send the collected data to the configured email address
### 🔹 2. Encrypt Collected Files
1. Navigate to functions folder:
   ```bash
cd functions
```
2. Run the _encrypt_files.py:
This will:
- Encrypt all files located in the files/ folder
- Move the encrypted versions to the encrypted_files/ directory.
### 🔹 3. Generate an Encryption Key


