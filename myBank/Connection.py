from myBank.Users import Users


class Connection(Users):

    def __init__(self, login, pwd):
        super().__init__()
        self.login = login
        self.pwd = pwd

        #check if user exists
        self.user_in = self.check_user(self.login)
