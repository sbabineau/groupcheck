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


class TestGetUser(unittest.TestCase):

    def setUp(self):
        with open('testdata/passwd.txt', 'r') as f:
            self.passwd = f.read()

        self.result = [
            groupcheck.User("root", "0"),
            groupcheck.User("daemon", "1"),
            groupcheck.User("bin", "2"),
            groupcheck.User("sys", "3"), 
            groupcheck.User("sync", "4")
        ]

    def testGetUserOutput(self):
        userlist = []
        for i in groupcheck.get_users(users=self.passwd):
            userlist.append(i)
        for i in xrange(5):
            self.assertEqual(self.result[i].username, userlist[i].username)
            self.assertEqual(self.result[i].gid, userlist[i].gid)


class TestGetValid(unittest.TestCase):

    def setUp(self):
        with open('testdata/group.txt', 'r') as f:
            self.group = f.read()

        self.result = [
            "0",
            "1",
            "2",
            "3",
            "4"
        ]

    def testGetValidOutput(self):
        self.assertEqual(groupcheck.get_valid(self.group), self.result)


if __name__ == "__main__":
    unittest.main()
