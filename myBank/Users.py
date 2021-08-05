from myBank.Account import Account


class Users(Account):
    users = [
        {'login': 'andri'}
    ]

    def __init__(self, name=None, login=None, age=None, gender=None, pwd=None):
        super().__init__()
        self.name = name
        self.login = login
        self.age = age
        self.gender = gender
        self.pwd = pwd

    def set_pwd(self, pwd):
        self.pwd = pwd

    def welcome(self):
        print(f'Welcome {self.name}')

    def check_user(self, username: str):
        for user in self.users:
            if username == user['login']:
                return True
            else:
                return False

