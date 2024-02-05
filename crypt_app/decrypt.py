from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

class DecryptUtil:
    def __init__(self,key):
        self.key = key

    def decrypt_value(self,string_to_decrypt):
        if not self.key:
            raise ValueError('Encryption key is not found.')
        try:
            cipher_suite = Fernet(self.key)
            decrypted_value = cipher_suite.decrypt(string_to_decrypt).decode()
            return decrypted_value
        except ValueError as ve:
            print('Key is not valid!')
    
    def read_from_file(self,filename):
        with open(filename,'rb') as file:
            return file.read()
        
    def read_dot_env_file(self,env_file,env_params):
        load_dotenv(env_file)
        env_vars = []
        for i in range(len(env_params)):
            env_var = self.__get_env_var(env_params[i])
            env_vars.append(self.decrypt_value(env_var))
        return env_vars

    def __get_env_var(self,env_key : str):
        return os.getenv(env_key)


# key: b'wi5ORv2XEq7yLyWA6L6O53q0Hjgi5JIJa2Px-H8_R5Y='
# pass: b'gAAAAABltYcqcIoM5OnawnNi2ogsgz-O88CbMfnnM-A6sy2NMhi_MslnNkt_uBmAXEoTuowfRWxIkBvA1ZVm881SkbAxHLIbuw=='
