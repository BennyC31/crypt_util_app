from cryptography.fernet import Fernet
import os
import base64

class EncryptUtil:
    def __init__(self,key=None):
        self.key = key

    def generate_new_key(self):
        return Fernet.generate_key()
    
    def get_os_key(self,key_name):
        self.os_key = os.environ.get(key_name)
        return self.os_key
    
    def encrypt_value(self,string_to_encrypt):
        if not self.key:
            raise ValueError('Encryption key is not found.')
        try:
            cipher_suite = Fernet(self.key)
            encrypted_value = cipher_suite.encrypt(string_to_encrypt.encode())
            return encrypted_value
        except ValueError as ve:
            print(f'Key is not valid: {ve}')

    def convert_to_base64_key(self,key_str):
        key_bytes = key_str.encode()
        base64_encoded = base64.urlsafe_b64encode(key_bytes)
        return base64_encoded.ljust(32,b'=')

    def encrypt_text(self,key_str,text):
        key = key_str
        if type(key_str) != bytes:
            key = self.convert_to_base64_key(key_str)
        cipher = Fernet(key)
        encrypted_text = cipher.encrypt(text.encode())
        return encrypted_text
    
    def write_new_key_to_file(self,filename,env_name='None'):
        with open(filename,'w') as file:
            file.write(f'{env_name}={self.generate_new_key()}')

    def write_encrypted_text_to_file(self,key_str,filename,text_to_encrypt):
        encrypted_text = self.encrypt_text(key_str=key_str,text=text_to_encrypt)
        with open(filename,'w') as file:
            file.write(f'encrypted_text={encrypted_text}')
    
    def write_encrypted_value_to_file(self,filename,encrypted_text):
        with open(filename,'wb') as file:
            file.write(encrypted_text)
    
    def write_to_env_file(self,filename : str,env_dict : dict):
        with open(filename,'w') as file:
            for k,v in env_dict.items():
                file.write(f"{k}={v.decode()}\n")

