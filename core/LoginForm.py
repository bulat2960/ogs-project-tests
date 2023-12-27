from tkinter import *
from tkinter import ttk

from functools import partial
from helpers.make_auth_link import make_auth_link
import secret_settings

class LoginForm: 
    def __init__(self, auth_callback, start_callback, stop_callback): 
        self.root = Tk()
        self.root.title("Monkey test")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.setup_link_field()
        self.setup_login_field()
        self.setup_password_field()

        ttk.Label(self.mainframe, text="Enter the data").grid(column=2, columnspan=1, row=0, sticky=(W, E))

        self.add_auth_button(auth_callback)
        self.add_start_button(start_callback)
        self.add_stop_button(stop_callback)

    def setup_login_field(self):
        ttk.Label(self.mainframe, text="Login").grid(column=1, columnspan=1, row=2, sticky=(W, E))

        self.login_var = StringVar(value=secret_settings.login)
        login_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.login_var)
        login_entry.grid(column=2, row=2, sticky=(W, E))

    def setup_password_field(self):
        ttk.Label(self.mainframe, text="Password").grid(column=1, columnspan=1, row=3, sticky=(W, E))

        self.password_var = StringVar(value=secret_settings.password)
        password_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.password_var)
        password_entry.grid(column=2, row=3, sticky=(W, E))

    def setup_link_field(self):
        ttk.Label(self.mainframe, text="Game link").grid(column=1, columnspan=1, row=1, sticky=(W, E))

        self.link_var = StringVar(value=secret_settings.link)
        link_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.link_var)
        link_entry.grid(column=2, row=1, sticky=(W, E))

    def make_link(self):
        return make_auth_link(self.link_var.get(), self.login_var.get(), self.password_var.get())

    def add_auth_button(self, auth_callback):
        ttk.Button(self.mainframe, text="Autorization", command=partial(auth_callback, self.make_link)).grid(column=2, row=4, sticky=(W, E))

    def add_start_button(self, start_callback): 
        ttk.Button(self.mainframe, text="Go", command=start_callback).grid(column=2, row=5, sticky=(W, E))

    def add_stop_button(self, stop_callback):
        ttk.Button(self.mainframe, text="Stop", command=stop_callback).grid(column=2, row=6, sticky=(W, E))

    def run(self):
        self.root.mainloop()

