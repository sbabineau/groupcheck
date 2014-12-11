import unittest
import groupcheck

class TestUserIsValidMethod(unittest.TestCase):

    def setUp(self):
        self.valid = ["1", "2", "3"]

    def testTrue(self):
        user = groupcheck.User("ellen", "1")
        self.assertTrue(user.is_valid(self.valid))

    def testFalseString(self):
        user = groupcheck.User("bob", "14")
        self.assertFalse(user.is_valid(self.valid))

    def testTrueInt(self):
        user = groupcheck.User("Mr. Number", 2)
        self.assertTrue(user.is_valid(self.valid))

    def testFalseInt(self):
        user = groupcheck.User("Mr. Number", 4)
        self.assertFalse(user.is_valid(self.valid))

    def testFalseNone(self):
        user = groupcheck.User("jerkface", None)
        self.assertFalse(user.is_valid(self.valid))

if __name__ == "__main__":
    unittest.main()
