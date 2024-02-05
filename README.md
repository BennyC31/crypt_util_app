# Encryption and Decryption Utility
Used to encrypt and decrypt sensitive data.

## Requirements
Used in Python projects.

## Processing
* Can be used to encrypt data and assined to an OS Environment variable.
    * Decryption needs the encryption key and the OS Environment variable to decrypt.
* Can be used to create an .env file.
    * Decryption needs the encryption key, the environment variables to decrypt.

## Version
0.1.0

## Authors
Benjamin Calderaio, Jr.

## License
None

## Available on Test PyPi
None

## Available on PyPi
None

## Usage Example
### Encrypt a password
encryptor = EncryptUtil()</br>
value_to_encrypt = 'testpWd'</br>
key = encryptor.generate_new_key()</br>
encryptor = EncryptUtil(key=key)</br>
os.environ['TEST_KEY'] = key</br>
encrypted_value = encryptor.encrypt_value(string_to_encrypt=value_to_encrypt)</br>
### Decrypt password
decryptor = DecryptUtil(key=key)</br>
decrypted_value = decryptor.decrypt_value(string_to_decrypt=encrypted_value)</br>
### Encrypt .env File
##### Note: please do not make the file public
file_path = '/path/project.env'</br>
encryptor = EncryptUtil(key=os.environ.get('TEST_KEY'))</br>
strings_to_encrypt = ['localhost','3306','test_schema']</br>
my_dict = {}</br>
my_dict['HOST'] = encryptor.encrypt_value(string_to_encrypt=strings_to_encrypt[0])</br>
my_dict['PORT'] = encryptor.encrypt_value(string_to_encrypt=strings_to_encrypt[1])</br>
my_dict['NAME'] = encryptor.encrypt_value(string_to_encrypt=strings_to_encrypt[2])</br>
encryptor.write_to_env_file(filename=file_path,env_dict=my_dict)
### Decrypt .env File
decryptor = DecryptUtil(key=os.environ.get('TEST_KEY'))</br>
env_params = ['HOST','PORT','NAME']</br>
env_vars = decryptor.read_dot_env_file(env_file=file_path,env_params=env_params)</br>