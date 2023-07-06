from random import randint

class Bank:
    numUsers = 0
    users = {}

    def __init__(self, user):
        self.user = user
        self.money = 0
        self.userid = Bank.idGenerator()

        Bank.numUsers += 1
        Bank.users[self.userid] = self.user

    @classmethod
    def showUsers(cls):
        if len(cls.users):
            for id, userName in cls.users.items():
                print(f'\nUser id: {id}\nUsername: {userName}')
            return 'All users in bank.'
        return 'No user registered yet.'

    @staticmethod
    def idGenerator():
        while True:
            id = randint(1000, 9999) #Fix so there can be infinite users
            if id not in Bank.users:
                return id

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, name):
        if name.isalpha():
            try:
                self._user =  ' '.join([final_name[0].upper() + final_name[1:len(name)].lower() for final_name in name.strip().split()])
            except:
                self._user = 'PlaceHolder'
        else:
            self._user = 'PlaceHolder'

    def increaseMoney(self, amount):
        self.money += amount
    
    def cashBack(self, amount):
        self.money -= amount

    def showBankAccount(self):
        return f"\n{'='*50}\n{self.user + ' bank': ^50}\nBank money: ${self.money}\nBank user id: {self.userid}\n{'='*50}\n"

class Wallet(Bank):
    def __init__(self, user):
        super().__init__(user)

        self.user = user
        self.walletMoney = 0

    def showWalletMoney(self):
        return f'You have ${self.walletMoney} in your wallet.'
    
    def recieveMoney(self, amount):
        self.walletMoney += amount

    def saveMoney(self, amount):
        if amount <= self.walletMoney:
            self.increaseMoney(amount)
            self.walletMoney -= amount
            return 'The operation was a success!'
        return 'You need more money.'
    
    def retireMoney(self, amount):
        if amount <= self.money:
            self.cashBack(amount)
            self.walletMoney += amount
            return 'The operation was a success!'
        return 'You need more money in your bank.'

    def showBankMoney(self):
        return f'You have ${self.money} in your bank.'


if __name__ == '__main__':
    while True:
        choice = input("\n1 - Register a new user\n2 - See all users\n3 - See user walletmoney\n\n>>> ").strip()
        if choice == '1':
            userName = input("\nInsert the user name: ").strip()
            userName = Wallet(userName)
            print(userName, type(userName))
        elif choice == '2':
            print(f'\n{Bank.showUsers()}')
        elif choice == '3':
            if Bank.users:
                print(f'\n{Bank.showUsers()}')
                while True:
                    userId = input("Enter user id or enter 0 to exit: ").strip()
                    if userId == '0':
                        break
                    elif int(userId) in Bank.users: #Fix this to make it possible to access money from a specific user's wallet
                        pass
            else:
                print('\nNo user registered yet.')
        else:
            print("\nUnknow choice.")
