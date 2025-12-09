from cryptography.fernet import Fernet

file_path = "C:\Users\PC-Service\OneDrive\Desktop\project\\cryptography\\"
encryption_key = "encryption_key.txt"

key = Fernet.generate_key()
file = open(file_path + encryption_key, "wb")
file.write(key)
file.close()