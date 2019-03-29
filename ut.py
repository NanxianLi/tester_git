import unittest
from app import *


class Add_Test(unittest.TestCase):
    def test_adding(self):
        self.assertEqual(adding(1,1), 3)


if __name__ == "__main__":
	unittest.main()