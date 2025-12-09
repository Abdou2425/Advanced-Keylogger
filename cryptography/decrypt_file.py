from cryptography.fernet import Fernet

key = "tT2M0xwaxM-ceVtoFXQFCpenQwWcSCvaqQd1IFRxn1w="

encrypted_file_path = "C:\Users\PC-Service\OneDrive\Desktop\project\\encrypted_files\\"
decrypted_file_path = "C:\Users\PC-Service\OneDrive\Desktop\project\\decrypted_files\\"

keys_information_e = "key_log_e.txt"
system_information_e = "system_info_e.txt"
clipboard_information_e = "clipboard_e.txt"
network_information_e = "network_info_e.txt"

encrypted_files = [ encrypted_file_path + keys_information_e,
                   encrypted_file_path + system_information_e,
                   encrypted_file_path + clipboard_information_e,
                   encrypted_file_path + network_information_e]


keys_information_d = "key_log_d.txt"
system_information_d = "system_info_d.txt"
clipboard_information_d = "clipboard_d.txt"
network_information_d = "network_info_d.txt"

decrypted_files = [decrypted_file_path + keys_information_d,
                   decrypted_file_path + system_information_d,
                   decrypted_file_path + clipboard_information_d,
                   decrypted_file_path +network_information_d]

count = 0
for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()
    
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)

    with open(decrypted_files[count], 'wb') as f:
        f.write(decrypted_data)

    count += 1
