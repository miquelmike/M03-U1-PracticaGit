import unittest
from security import validar_password

class TestPassword(unittest.TestCase):
    def test_password_corta(self):
        self.assertFalse(validar_password("abc"))

    def test_password_llarga(self):
        self.assertTrue(validar_password("abcdefghij"))

if __name__ == "__main__":
    unittest.main()
