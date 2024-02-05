import setuptools

with open('README.md','r') as rfile:
    long_description = rfile.read()

setuptools.setup(
    include_package_data=True,
    name='encrypt-decrypt-util',
    version='0.1.0',
    description='Utility used for encrypting and decrypting data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['cryptography==42.0.1','python-dotenv==1.0.1'],
    url='https://github.com/BennyC31/crypt_util_app.git',
    author='Benjamin Calderaio, Jr.',
    author_email='bencalderaio@gmail.com',
    packages=['crypt_app'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'TOPIC :: Security :: Cryptography',
        'License :: Free for non-commercial use',
        'Topic :: Utilities'
    ]
)