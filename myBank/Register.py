from myBank.Users import Users


class Register(Users):

    def __init__(self, name, login, age, gender, pwd):
        super().__init__(name, login, age, gender, 'test')
        self.set_pwd(pwd)  # ToDo get Entry pwd
        if 'test' == self.pwd:
            print("Your password need to be changed")

    def set_pwd(self, pwd):
        self.pwd = pwd
