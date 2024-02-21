import unittest

from zad6 import caesar_cipher


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_positive_shift(self):
        plaintext = "Hello, World!"
        shift = 3
        encrypted_text = caesar_cipher(plaintext, shift)
        self.assertEqual(encrypted_text, "Khoor, Zruog!")

    def test_encrypt_negative_shift(self):
        plaintext = "Hello, World!"
        shift = -3
        encrypted_text = caesar_cipher(plaintext, shift)
        self.assertEqual(encrypted_text, "Ebiil, Tloia!")

    def test_encrypt_with_float_key(self):
        plaintext = "Hello, World!"
        float_shift = 2.5
        with self.assertRaises(ValueError):
            caesar_cipher(plaintext, float_shift)

if __name__ == "__main__":
    unittest.main()
