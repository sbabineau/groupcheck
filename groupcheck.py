#!/usr/bin/env python
import subprocess


class user(object):

    def __init__(self, username, gid):
        self.username = username
        self.gid = gid

    def is_valid(self, valid):
        if self.gid in valid:
            return True
        return False


def get_valid():
    result = []
    groups = subprocess.check_output(["getent", "group"])
    groups = groups.splitlines()
    for i in groups:
        i = i.split(":")
        result.append(i[2])
    return result


def get_users():
    users = subprocess.check_output(["getent", "passwd"])
    users = users.splitlines()
    for i in users:
        i = i.split(":")
        yield user(i[0], i[3])


def groupcheck(valid=get_valid(), users=get_users()):
    for i in users:
        if not i.is_valid(valid):
            print "user %s has invalid group id %s" % (i.username, i.gid)


if __name__ == "__main__":
    groupcheck()
