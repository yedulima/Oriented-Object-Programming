import json
import os
from time import sleep

class Instagram:
    users = json.load(open('users.json', 'r'))

    def __init__(self, username, display_name=f'user{len(users) + 1}'):
        self.addUser(username, display_name)
        self.user = username

    @classmethod
    def banUser(cls, username):
        if f'@{username}'.lower() in cls.users.keys():
            for user in cls.users.keys():
                if user == f'@{username}'.lower():
                    del cls.users[user]
                    json.dump(cls.users, open('users.json', 'w'))
                    return 'The operation was a success!'
        return 'Informed user not found.'

    @classmethod
    def addUser(cls, username, display_name=f'user{len(users) + 1}'):
        if f'@{username}'.lower() not in cls.users:
            cls.users[f'@{username}'.lower()] = {'UserId': (len(cls.users) + 1),'Display name': display_name, 'Posts': 0, 'Followers': 0, 'Following': 0}
            os.mkdir(f'usersImages/@{username.lower()}_posts')
            json.dump(cls.users, open('users.json', 'w'))
            return 'The operation was a success!'
        return 'User already exist.'

if __name__ == '__main__':
    p1 = Instagram('Edu', 'du')
    print(p1.users)
    print(p1.addUser('Edu'))
    print(p1.users)
    #print(p1.addUser('Miguel'))
    sleep(7)
    print(p1.banUser('Edu'))