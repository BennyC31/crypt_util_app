import pytest
import os
from crypt_app.encrypt import *


class TestEncrypt:
    def setup_method(self):
        self.encryptor = EncryptUtil()
        self.os_key = 'testKey'
        os.environ['TEST_KEY'] = self.os_key

    def teardown_method(self):
        if os.path.exists('encrypted.dat'):
            os.remove('encrypted.dat')
        if os.path.exists('encrypted_none.dat'):
            os.remove('encrypted_none.dat')
        if os.path.exists('encrypted_text.dat'):
            os.remove('encrypted_text.dat')
        if os.path.exists('encpwd.pwd'):
            os.remove('encpwd.pwd')
        if os.path.exists('encrypted_text.pwd'):
            os.remove('encrypted_text.pwd')
        if os.path.exists('encrypted_text_alt.pwd'):
            os.remove('encrypted_text_alt.pwd')

    def test_generate_new_key(self):
        new_key = None
        new_key = self.encryptor.generate_new_key()
        # print(f'new_key={new_key}')
        assert new_key is not None
    
    def test_get_os_key(self):
        key_to_test = self.encryptor.get_os_key('TEST_KEY')
        assert key_to_test == self.os_key

    def test_encrypt_value(self):
        encryptor1 = EncryptUtil(self.encryptor.generate_new_key())
        value_to_encrypt = 'testpWd'
        encrypted_value = encryptor1.encrypt_value(string_to_encrypt=value_to_encrypt)
        assert encrypted_value is not None

    def test_encrypt_text(self):
        key = 'testKey1testKey1testKey1testKey1'
        value_to_encrypt = 'testpWd'
        encrypted_value = self.encryptor.encrypt_text(key_str=key,text=value_to_encrypt)
        assert encrypted_value is not None
    
    def test_encrypt_text_new_key(self):
        key = self.encryptor.generate_new_key()
        value_to_encrypt = 'testpWd'
        encrypted_value = self.encryptor.encrypt_text(key_str=key,text=value_to_encrypt)
        assert encrypted_value is not None

    def test_write_new_key_to_file(self):
        self.encryptor.write_new_key_to_file('encrypted.dat','encrypt_key')
        assert os.path.exists('encrypted.dat')
        self.encryptor.write_new_key_to_file('encrypted_none.dat')
        assert os.path.exists('encrypted_none.dat')

    def test_write_encrypted_text_to_file(self):
        key = 'testKey1testKey1testKey1testKey1'
        value_to_encrypt = 'testpWd'
        self.encryptor.write_encrypted_text_to_file(key_str=key,filename='encrypted_text.dat',text_to_encrypt=value_to_encrypt)
        assert os.path.exists('encrypted_text.dat')

    def test_write_encrypted_value_to_file(self):
        key = self.encryptor.generate_new_key()
        encryptor = EncryptUtil(key=key)
        value_to_encrypt = 'myPassW0rd1'
        encrypted_value = encryptor.encrypt_value(string_to_encrypt=value_to_encrypt)
        encryptor.write_encrypted_value_to_file(filename='encpwd.pwd',encrypted_text=encrypted_value)
        assert os.path.exists('encpwd.pwd')

    def test_write_to_env_file(self):
        file_path = os.path.join(os.path.dirname(__file__),'config','test_env.env')
        key = self.encryptor.generate_new_key()
        encryptor = EncryptUtil(key=key)
        my_dict = {}
        my_dict['HOST'] = encryptor.encrypt_value(string_to_encrypt='localhost')
        my_dict['PORT'] = encryptor.encrypt_value(string_to_encrypt='3306')
        my_dict['NAME'] = encryptor.encrypt_value(string_to_encrypt='test_schema')
        my_dict['DBUSER'] = encryptor.encrypt_value(string_to_encrypt='benc')
        my_dict['PASSWORD'] = encryptor.encrypt_value(string_to_encrypt='myPassW0rd1')
        encryptor.write_to_env_file(filename=file_path,env_dict=my_dict)
        assert os.path.exists(file_path)