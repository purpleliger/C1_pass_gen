# test_C1_password_generator.py

import unittest
from C1_password_generator import gen_password

class TestPassGen(unittest.TestCase):
    def test_gen_password(self):
        # Test the function with different length parameters
        password_length= 9
        generated_pass = gen_password(password_length)
        self.assertEqual(len(generated_pass), password_length)

        password_length= 14
        generated_pass = gen_password(password_length)
        self.assertEqual(len(generated_pass), password_length)

if __name__ == '__main__':
    unittest.main()

