from caesar_cipher import encrypt, decrypt
import unittest

class CaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt(25, "world"), "vnqkc")
        self.assertEqual(encrypt(10, "hello world"), "rovvy gybvn")
    
    def test_decrypt(self):
        self.assertEqual(decrypt(25, "vnqkc"), "world")
        self.assertEqual(decrypt(10, "rovvy gybvn"), "hello world")
