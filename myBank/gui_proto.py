import tkinter as tk
from tkinter import messagebox
from Users import Users


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.area_list = ['name', 'login', 'age', 'gender', 'pwd']

        # Area and Button
        # name
        self.name = tk.Label(self)
        self.name_entry = tk.Entry(self)

        # login
        self.login = tk.Label(self)
        self.login_entry = tk.Entry(self)

        # age
        self.age = tk.Label(self)
        self.age_entry = tk.Entry(self)

        # gender
        self.gender = tk.Label(self)
        self.gender_entry = tk.Entry(self)

        # pwd
        self.pwd = tk.Label(self)
        self.pwd_entry = tk.Entry(self)

        self.hi_there = tk.Button(self)
        self.quit = tk.Button(self, text="Cancel", fg="red",
                              command=self.master.destroy)

        self.message = tk.Label(self)

        # packing
        self.pack()

        self.create_area()
        self.create_widgets()

    def create_area(self):
        # Form Area
        self.name["text"] = "Your name"
        self.login["text"] = "Your login"
        self.age["text"] = "Your age"
        self.gender["text"] = "Your gender"
        self.pwd["text"] = "Your password"
        self.message["text"] = ""

        self.master.geometry('400x400')

        self.pack_with_name()

        self.message.pack()

    def create_widgets(self):
        self.hi_there["text"] = "Register"
        self.hi_there["command"] = self.register_account
        self.hi_there.pack(side="top")
        self.quit.pack(side="bottom")

    def register_account(self):
        name = self.name_entry.get()
        login = self.login_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        pwd = self.pwd_entry.get()

        user_test = Users()
        if user_test.check_user(login):
            self.message["text"] = "Login Already Exists"
        else:
            user_account = Users(name, login, age, gender, pwd)
            self.message["text"] = "Account created"

    def pack_with_name(self):
        for area in self.area_list:
            exec(f'self.{area}.pack()')
            exec(f'self.{area}_entry.pack()')

    # def connect_account(self):
    #    user_account = ac(name, age, gender)
    #    user_account.show_info()
    #    user_account.show_balance()
