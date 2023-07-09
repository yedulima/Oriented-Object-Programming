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
        username = f'@{username}'.lower()
        if username in cls.users.keys():
            for user in cls.users.keys():
                if user == username:
                    try:
                        os.rmdir(os.path.join(os.getcwd().replace('\\', '/') + "/usersImages", f'{user}-posts'))
                    except:
                        print("Unable to remove posts from this user.")
                    del cls.users[user]
                    json.dump(cls.users, open('users.json', 'w'))
                    return 'The operation was a success!'
        return 'Informed user not found.'

    @classmethod
    def addUser(cls, username, display_name=f'user{len(users) + 1}'):
        if f'@{username}'.lower() not in cls.users:
            cls.users[f'@{username}'.lower()] = {'UserId': (len(cls.users) + 1),'Display name': display_name, 'Posts': 0, 'Followers': 0, 'Following': 0}
            try:
                os.mkdir(f'usersImages/@{username.lower()}-posts')
            except:
                print("User already exist.")
            json.dump(cls.users, open('users.json', 'w'))
            return 'The operation was a success!'
        return 'User already exist.'

if __name__ == '__main__':
    p1 = Instagram('Edu', 'du')
    sleep(5)
    print(p1.banUser('Edu'))