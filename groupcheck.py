#!/usr/bin/env python
import subprocess
import sys


class User(object):

    def __init__(self, username, gid):
        self.username = username
        self.gid = gid

    def is_valid(self, valid):
        if str(self.gid) in valid:
            return True
        return False

    def __str__(self):
        return "{username: %s, gid: %s}" % (self.username, self.gid)


def get_valid(groups=None):
    result = []
    if groups is None:
        groups = subprocess.check_output(["getent", "group"])
    groups = groups.splitlines()
    for i in groups:
        i = i.split(":")
        result.append(i[2])
    return result


def get_users(users=None):
    if users is None:
        users = subprocess.check_output(["getent", "passwd"])
    users = users.splitlines()
    for i in users:
        i = i.split(":")
        yield User(i[0], i[2])


def groupcheck(users=get_users(), valid=get_valid()):
    """Takes a list of valid gids and compares a user list to it. valid should
    be given a list of strings. users should be a string with the contents of a
    linux /etc/passwd file"""
    fail_count = 0
    for i in users:
        if not i.is_valid(valid):
            fail_count += 1
            print "user %s has invalid group id %s" % (i.username, i.gid)
    if fail_count == 0:
        print "No users have an invalid group id"


if __name__ == "__main__":
    if len(sys.argv) == 3:
        u, g = sys.argv[1], sys.argv[2]
        with open(u, 'r') as f:
            u = f.read()
        with open(g, 'r') as f:
            g = f.read()
        groupcheck(users=get_users(u), valid=get_valid(g))
    else:
        groupcheck()
