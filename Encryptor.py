from cryptography.fernet import Fernet
###

###




def decrypt():
    with open("key.txt", "r") as key_file:
        f = Fernet(key_file.read())
    with open("APIKEY.txt", "r") as api_file:
        encrypted_message = api_file.read()
    return f.decrypt(encrypted_message).decode()