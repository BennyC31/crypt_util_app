import pytest
import os
from crypt_app.decrypt import *
from crypt_app.encrypt import *


class TestDecrypt:
    def setup_method(self):
        # 'hrpPY_EAAUaNhRhPj5HCdXABaaFabLfqImGMiUkP8aE='
        self.os_key = 'hrpPY_EAAUaNhRhPj5HCdXABaaFabLfqImGMiUkP8aE='
        os.environ['TEST_KEY'] = self.os_key
        
    def teardown_method(self):
        pass

    def test_decrypt_value_os_key(self):
        encryptor = EncryptUtil(os.environ.get('TEST_KEY'))
        decryptor = DecryptUtil(os.environ.get('TEST_KEY'))
        string_to_encrypt='testpWd1'
        encrypted_value = encryptor.encrypt_value(string_to_encrypt=string_to_encrypt)
        decrypted_value = decryptor.decrypt_value(string_to_decrypt=encrypted_value)
        assert string_to_encrypt == decrypted_value

    def test_decrypt_value_from_file(self):
        encryptor = EncryptUtil(os.environ.get('TEST_KEY'))
        decryptor = DecryptUtil(os.environ.get('TEST_KEY'))
        # print(f"Test_key={os.environ.get('TEST_KEY')}")
        string_to_encrypt='testpWd1'
        encrypted_value = encryptor.encrypt_value(string_to_encrypt=string_to_encrypt)
        encryptor.write_encrypted_value_to_file(filename='encrypted_text.pwd',encrypted_text=encrypted_value)
        encrypted_value_to_decrypt = decryptor.read_from_file(filename='encrypted_text.pwd')
        decrypted_value = decryptor.decrypt_value(string_to_decrypt=encrypted_value_to_decrypt)
        assert string_to_encrypt == decrypted_value

    def test_decrypt_value_from_file_alt(self):
        encryptor = EncryptUtil(os.environ.get('TEST_KEY'))
        decryptor = DecryptUtil(os.environ.get('TEST_KEY'))
        string_to_encrypt='testpW0d1'
        encryptor.write_encrypted_value_to_file(filename='encrypted_text_alt.pwd',
                                                encrypted_text=encryptor.encrypt_value(string_to_encrypt=string_to_encrypt))
        decrypted_value = decryptor.decrypt_value(string_to_decrypt=decryptor.read_from_file(filename='encrypted_text_alt.pwd'))
        assert string_to_encrypt == decrypted_value

    def test_decrypt_value_new_key(self):
        encryptor = EncryptUtil()
        value_to_encrypt = 'testpWd'
        key = encryptor.generate_new_key()
        encryptor = EncryptUtil(key=key)
        # encrypted_value = encryptor.encrypt_text(key_str=key,text=value_to_encrypt)
        encrypted_value = encryptor.encrypt_value(string_to_encrypt=value_to_encrypt)
        decryptor = DecryptUtil(key=key)
        decrypted_value = decryptor.decrypt_value(string_to_decrypt=encrypted_value)
        assert value_to_encrypt == decrypted_value

    def test_read_dot_env_file(self):
        file_path = os.path.join(os.path.dirname(__file__),'config','test_env_decrypt.env')
        encryptor = EncryptUtil(os.environ.get('TEST_KEY'))
        decryptor = DecryptUtil(os.environ.get('TEST_KEY'))
        strings_to_encrypt = ['localhost','3306','test_schema','benc','myPassW0rd1']
        my_dict = {}
        my_dict['HOST'] = encryptor.encrypt_value(string_to_encrypt=strings_to_encrypt[0])
        my_dict['PORT'] = encryptor.encrypt_value(string_to_encrypt=strings_to_encrypt[1])
        my_dict['NAME'] = encryptor.encrypt_value(string_to_encrypt=strings_to_encrypt[2])
        my_dict['DBUSER'] = encryptor.encrypt_value(string_to_encrypt=strings_to_encrypt[3])
        my_dict['PASSWORD'] = encryptor.encrypt_value(string_to_encrypt=strings_to_encrypt[4])
        encryptor.write_to_env_file(filename=file_path,env_dict=my_dict)
        env_params = ['HOST','PORT','NAME','DBUSER','PASSWORD']
        env_vars = decryptor.read_dot_env_file(env_file=file_path,env_params=env_params)
        assert strings_to_encrypt[0] == env_vars[0]
        assert strings_to_encrypt[1] == env_vars[1]
        assert strings_to_encrypt[2] == env_vars[2]
        assert strings_to_encrypt[3] == env_vars[3]
        assert strings_to_encrypt[4] == env_vars[4]